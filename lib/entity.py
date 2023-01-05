from pathlib import Path

import yaml

from lib.tools import save_json


class Entity(dict):
    """A Thing."""

    def __init__(self, datafile):
        """Constructor."""
        self.datafile = Path(datafile)
        self.identifier = self.datafile.stem
        self.load_data()
        self.populate()

    def load_data(self):
        """Load the YAML."""
        self.data = yaml.safe_load(Path(self.datafile).read_text(encoding="utf-8"))

    def populate(self):
        """Populate ourself."""
        self["@context"] = "https://schema.org"
        if "website" in self.data:
            self["url"] = self.data["website"]

        self.refine()

    def refine(self):
        """Placeholder to be defined in subclass."""

    def save(self, outroot="dist"):
        """Write ourselves to a disk."""
        out_dir = Path(str(self.datafile.parent).replace("data", outroot))
        save_json(self, out_dir, f"{self.datafile.stem}.json")
