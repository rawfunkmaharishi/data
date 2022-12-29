class Performer(dict):
    """A Performer."""

    def __init__(self, data):
        """Constructor."""

        self["@type"] = "MusicGroup"
        self["name"] = data["name"]
        if "website" in data:
            self["sameAs"] = data["website"]
