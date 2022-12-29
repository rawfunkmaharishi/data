from lib.entity import Entity


class Venue(Entity):
    """A Venue."""

    def refine(self):
        """Add our specific data."""
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
