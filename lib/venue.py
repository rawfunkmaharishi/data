from pathlib import Path

import yaml


class Venue(dict):
    """A Venue."""

    def __init__(self, datafile) -> None:
        """Constructor."""

        self.data = yaml.safe_load(
            Path("data", "venues", datafile).read_text(encoding="utf-8")
        )

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
