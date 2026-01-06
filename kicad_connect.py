import json
from pathlib import Path

from kipy import KiCad
from kipy.proto.common.types import DocumentType

CFG = Path.home() / ".config/kicad/9.0/kicad_common.json"

EDITORS_TO_FETCH = [
    {"name": "Footprint Editor", "type": DocumentType.DOCTYPE_FOOTPRINT, "icon": ""},
    {"name": "Symbol Editor", "type": DocumentType.DOCTYPE_SYMBOL, "icon": ""},
    {"name": "PCB Editor", "type": DocumentType.DOCTYPE_PCB, "icon": "pcbnew"},
    {
        "name": "Schematic Editor",
        "type": DocumentType.DOCTYPE_SCHEMATIC,
        "icon": "eeschema",
    },
]
DEFAULT_EDITOR = {"name": "Main menu", "type": None, "icon": ""}


class KiCadConnect:
    def __init__(self) -> None:
        self.kicad = KiCad()
        self.saved_project_name = None

    def editor_is_open(self, doc_type: DocumentType.ValueType):
        try:
            self.kicad.get_open_documents(doc_type)
            return True
        except Exception:
            return False

    def get_opened_editor(self):
        self.kicad.get_version()
        for editor in EDITORS_TO_FETCH:
            if self.editor_is_open(editor["type"]):
                return editor
        return DEFAULT_EDITOR

    def get_project_name_by_path(self):
        try:
            with open(CFG) as f:
                data = json.load(f)
            wd = data.get("system")["working_dir"]
            if not wd:
                return None
            wd = Path(wd)
            return wd.name

        except Exception:
            return None

    def get_project_name_with_editor(self):
        for editor in EDITORS_TO_FETCH:
            try:
                resp = self.kicad.get_open_documents(editor["type"])
                return Path(resp[0].board_filename).stem
            except Exception:
                pass

    def get_project_name(self):
        project_name_by_path = self.get_project_name_by_path()
        project_name_with_editor = self.get_project_name_with_editor()
        if project_name_with_editor:
            self.saved_project_name = project_name_with_editor
        return (
            project_name_with_editor or self.saved_project_name or project_name_by_path
        )


if __name__ == "__main__":
    kicad = KiCadConnect()
    print("path project name", kicad.get_project_name_by_path())
    print("editor project name", kicad.get_project_name_with_editor())
    try:
        print(kicad.get_opened_editor())
    except Exception as e:
        print(f"An error occurred: {e}")
