import json
from pathlib import Path

from lib.entity import Entity
from lib.performer import Performer


class Gig(Entity):
    """A Gig."""

    def refine(self):
        """Add our specific data."""
        self["@type"] = "MusicEvent"
        self["startDate"] = self.datestamp

        location = json.loads(
            Path("dist", "venues", f"{self.data['venue']}.json").read_text(
                encoding="utf-8"
            )
        )
        del location["@context"]
        self["location"] = location
        self["name"] = f"Raw Funk Maharishi live at {location['name']}"

        self["sameAs"] = [f"https://rawfunkmaharishi.uk/gigs/{'/'.join(self.id_bits)}"]

        if "facebook_id" in self.data:
            self["sameAs"].append(
                f"https://facebook.com/events/{self.data['facebook_id']}/"
            )

        if "website" in self.data:
            self["sameAs"].append(self.data["website"])

        if len(self["sameAs"]) == 1:
            self["sameAs"] = self["sameAs"][0]

        self["performer"] = [
            Performer(
                {
                    "name": "Raw Funk Maharishi",
                    "website": "https://rawfunkmaharishi.uk/",
                }
            )
        ]

        if "other_bands" in self.data:
            self["performer"] += list(map(Performer, self.data["other_bands"]))

        if len(self["performer"]) == 1:
            self["performer"] = self["performer"][0]

        if "price" in self.data:
            self["offers"] = {
                "@type": "offer",
                "price": self.data["price"],
                "priceCurrency": "GBP",
            }

        self["offSchema"] = {"nameBits": self.id_bits}
        if isinstance(self["sameAs"], list):
            self["offSchema"]["hasMoreInfo"] = True

    @property
    def datestamp(self):
        """Extract the datestamp."""
        date = "-".join(self.id_bits[:3])
        return f"{date}T{self.data['time']}"

    @property
    def id_bits(self):
        """Pull out the bits from the filename."""
        bits = self.datafile.stem.split("-")
        return [bits[0]] + [bits[1]] + [bits[2]] + ["-".join(bits[3:])]
