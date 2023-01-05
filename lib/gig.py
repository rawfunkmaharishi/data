from pathlib import Path

from lib.entity import Entity
from lib.performer import Performer
from lib.raw_funk_maharishi import RawFunkMaharishi
from lib.tools import load_and_decontext


class Gig(Entity):
    """A Gig."""

    def refine(self):
        """Add our specific data."""
        self["@type"] = "MusicEvent"
        self["startDate"] = self.datestamp

        self["location"] = load_and_decontext(
            Path("dist", "venues", f"{self.data['venue']}.json")
        )

        self["name"] = f"Raw Funk Maharishi live at {self['location']['name']}"
        self["url"] = f"/gigs/{'/'.join(self.id_bits)}"

        if self.same_as:
            self["sameAs"] = self.same_as

        self["performer"] = [RawFunkMaharishi(with_context=False)]

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

        if "youtube_id" in self.data:
            self["recordedIn"] = {
                "@type": "VideoObject",
                "@id": f"https://www.youtube.com/watch?v={self.data['youtube_id']}",
                "name": self["name"],
                "description": self["name"],
                "uploadDate": "-".join(self.id_bits[:3]),
                "thumbnailUrl": (
                    f"https://img.youtube.com/vi/{self.data['youtube_id']}/default.jpg"
                ),
                "embedUrl": f"https://www.youtube.com/embed/{self.data['youtube_id']}",
            }

        if "promoter" in self.data:
            self["organizer"] = {
                "@type": "Organization",
                "name": self.data["promoter"],
            }

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

    @property
    def same_as(self):
        """Generate `sameAs`."""
        same = []
        if "facebook_id" in self.data:
            same.append(f"https://facebook.com/events/{self.data['facebook_id']}/")

        if "website" in self.data:
            same.append(self.data["website"])

        return same
