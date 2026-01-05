from kipy import KiCad
from kipy.proto.common.types import DocumentType

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
DEFAULT_EDITOR = {"name": "Main menu", "type": None}


def editor_is_open(kicad, doc_type: DocumentType.ValueType):
    try:
        kicad.get_open_documents(doc_type)
        return True
    except Exception:
        return False


def get_opened_editor():
    kicad = KiCad()
    kicad.get_version()
    for editor in EDITORS_TO_FETCH:
        if editor_is_open(kicad, editor["type"]):
            return editor
    return DEFAULT_EDITOR


if __name__ == "__main__":
    print(get_opened_editor())
