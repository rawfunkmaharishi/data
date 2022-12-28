import json
from pathlib import Path

import yaml


class Venue(dict):
    """A Venue."""

    def __init__(self, datafile) -> None:
        """Constructor."""

        self.datafile = Path("data", "venues", datafile)
        self.data = yaml.safe_load(Path(self.datafile).read_text(encoding="utf-8"))

        self["@context"] = "https://schema.org"
        self["@type"] = "Place"
        self["address"] = {
            "@type": "PostalAddress",
            "addressCountry": "United Kingdom",
            "streetAddress": f"{self.data['address']}, {self.data['postcode']}",
        }
        self["geo"] = {
            "@type": "GeoCoordinates",
            "latitude": self.data["latitude"],
            "longitude": self.data["longitude"],
        }
        self["name"] = self.data["name"]

        if "website" in self.data:
            self["sameAs"] = self.data["website"]

    def save(self, outroot="dist"):
        """Write ourselves to a disk."""
        venues_dir = Path(outroot, "venues")
        venues_dir.mkdir(exist_ok=True, parents=True)
        Path(venues_dir, f"{self.datafile.stem}.json").write_text(
            json.dumps(self, sort_keys=True), encoding="utf-8"
        )
