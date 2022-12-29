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

        self["startDate"] = "2022-12-15T21:00"

        location = json.loads(
            Path("dist", "venues", f"{self.data['venue']}.json").read_text(
                encoding="utf-8"
            )
        )
        del location["@context"]
        self["location"] = location
        self["name"] = f"Raw Funk Maharishi live at {location['name']}"

        self["sameAs"] = "https://rawfunkmaharishi.uk/gigs/2022/12/15/luna"
