import json
from pathlib import Path


def load_and_decontext(item):
    """Load JSON and pop the unwanted `@context` key."""
    data = json.loads(item.read_text(encoding="utf-8"))
    data.pop("@context")

    return data


def save_json(data, *path):
    """Save as JSON."""
    fullpath = Path(*path)
    fullpath.parent.mkdir(exist_ok=True, parents=True)
    fullpath.write_text(json.dumps(data, sort_keys=True, indent=4), encoding="utf-8")
