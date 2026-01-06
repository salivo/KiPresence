import signal
import subprocess
import sys
import time

from pypresence import Presence
from pypresence.types import ActivityType

from kicad_connect import KiCadConnect

client_id = "1337552550454366250"
RPC = Presence(client_id)

kicad_connect = KiCadConnect()

global_run = True


def shutdown(signum, frame):
    global global_run
    if global_run:
        global_run = False
        print("Stopping service...")
    else:
        sys.exit(0)


signal.signal(signal.SIGINT, shutdown)
signal.signal(signal.SIGTERM, shutdown)


def is_kicad_running():
    result = subprocess.run(["pgrep", "-x", "kicad"], stdout=subprocess.DEVNULL)
    return result.returncode == 0


def discord_logic(start_time):
    editor = kicad_connect.get_opened_editor()
    project_name = kicad_connect.get_project_name()
    project_string = ""
    if project_name:
        project_string = f"Developing: {project_name}"
    if editor["name"] == "Main menu":
        RPC.update(
            state=project_string,
            details="KiCad",
            name="KiCad",
            activity_type=ActivityType.COMPETING,
            large_image="icon_kicad",
            large_text="In main menu",
            start=start_time,
        )
    else:
        RPC.update(
            state=project_string,
            details="KiCad",
            name="KiCad",
            activity_type=ActivityType.COMPETING,
            small_image="icon_kicad",
            small_text="KiCad",
            large_image=editor["icon"],
            large_text=editor["name"],
            start=start_time,
        )


def poll_kicad_is_running():
    running = False
    activity_start_time = None
    while global_run:
        if not running:
            if is_kicad_running():
                print("KiCad Started")
                kicad_connect.reconnect()
                activity_start_time = int(time.time())
                running = True
                time.sleep(2)
                try:
                    RPC.connect()
                except Exception as e:
                    print(f"Error connecting to Discord RPC: {e}")
                    running = False
                continue
            else:
                try:
                    RPC.clear()
                except Exception:
                    pass
        else:
            try:
                discord_logic(activity_start_time)
            except Exception as e:
                print(f"Error occurred: {e}")
                running = False
                continue
        time.sleep(15)


if __name__ == "__main__":
    poll_kicad_is_running()
