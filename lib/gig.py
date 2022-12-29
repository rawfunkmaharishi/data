import json
from pathlib import Path

from lib.entity import Entity


class Gig(Entity):
    """A Gig."""

    def refine(self):
        """Add our specific data."""
        self["@type"] = "MusicEvent"
        self["performer"] = {
            "@type": "MusicGroup",
            "name": "Raw Funk Maharishi",
            "sameAs": "//rawfunkmaharishi.uk/",
        }

        self["startDate"] = self.datestamp

        location = json.loads(
            Path("dist", "venues", f"{self.data['venue']}.json").read_text(
                encoding="utf-8"
            )
        )
        del location["@context"]
        self["location"] = location
        self["name"] = f"Raw Funk Maharishi live at {location['name']}"

        self["sameAs"] = f"https://rawfunkmaharishi.uk/gigs/{'/'.join(self.id_bits)}"

    @property
    def datestamp(self):
        """Extract the datestamp."""
        date = "-".join(self.id_bits[:3])
        return f"{date}T{self.data['time']}"

    @property
    def id_bits(self):
        """Pull out the bits from the filename."""
        return self.datafile.stem.split("-")
