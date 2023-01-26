from lib.entity import Entity


class Venue(Entity):
    """A Venue."""

    def refine(self):
        """Add our specific data."""
        self["@type"] = "Place"
        self["address"] = {
            "@type": "PostalAddress",
            "addressCountry": "United Kingdom",
            "postalCode": self.data["postcode"],
            "streetAddress": self.data["address"],
        }
        self["geo"] = {
            "@type": "GeoCoordinates",
            "latitude": self.data["latitude"],
            "longitude": self.data["longitude"],
        }
        self["name"] = self.data["name"]

        if "image" in self.data:
            self["image"] = {
                "@type": "ImageObject",
                "contentUrl": f"/venues/{self.data['image']}",
                "name": self["name"],
            }
