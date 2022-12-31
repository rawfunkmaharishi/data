from lib.entity import Entity


class Person(Entity):
    """A Band Mamber."""

    def refine(self):
        """Add our specific data."""

        self["@type"] = "Person"
        self["name"] = self.data["name"]
        self["image"] = f"https://rawfunkmaharishi.uk/the-band/{self.data['image']}"

        self["offSchema"] = {}
        self["offSchema"]["image"] = self.data["image"]
