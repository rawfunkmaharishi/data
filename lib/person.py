from lib.entity import Entity


class Person(Entity):
    """A Band Mamber."""

    def refine(self):
        """Add our specific data."""

        self["@type"] = "Person"
        self["name"] = self.data["name"]
        self["image"] = {
            "@type": "ImageObject",
            "contentUrl": f"/the-band/{self.data['image']}",
            "name": self["name"],
        }
