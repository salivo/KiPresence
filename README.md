# KiPresence

**KiCad Discord Rich Presence** – a small system service that updates your Discord status with your KiCad activity.
## Features
- Shows your current project name
- Shows which editor you are working in
   - Currently supports Schematic and PCB editors
- Displays time spent working in KiCad

## Showcase
<img width="400" alt="demo" src="https://github.com/user-attachments/assets/10c77668-9240-43b5-b128-d70d8e297685" />
<img width="400" alt="demo_sheme" src="https://github.com/user-attachments/assets/3feb9537-1f6c-4a5c-b45e-e7d1d828c148" />
<img width="400" alt="demo_pcb" src="https://github.com/user-attachments/assets/ea42b74e-2597-4c6f-b9db-c48e0897c7cc" />

---

## Installation

1. Clone this repo
2. Install with pacman:
```bash
cd KiPresence
makepkg -si
```
4. Enable the systemd service:
 ```bash
 sudo systemctl enable --user --now kipresence.service
 ```

## Usage

* The service will automatically start and update your Discord status.
* To check the service status:

  ```bash
  systemctl status kipresence.service
  ```

### Manual building

```bash
# enter source directory
cd <source_dir>

# create virtual environment
python -m venv venv

# activate virtual environment
source venv/bin/activate

# install dependencies
python -m pip install -r requirements.txt

# build binary
pyinstaller --onefile --clean --strip kipresence.py

# run
./dist/kipresence
```
## License

MIT License – see `LICENSE` file.

---
