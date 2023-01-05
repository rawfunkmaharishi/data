from pathlib import Path

from lib.performer import Performer
from lib.tools import load_and_decontext, save_json


class RawFunkMaharishi(Performer):
    """The Band."""

    def __init__(self, with_context=True):
        """Constructor."""
        super().__init__(
            {"name": "Raw Funk Maharishi", "website": "https://rawfunkmaharishi.uk/"}
        )

        if with_context:
            self["@context"] = "https://schema.org"

        self["member"] = list(
            map(
                load_and_decontext,
                list(Path("dist/people").glob("*.json")),
            )
        )

    def save(self, outroot="dist"):
        """Write ourselves to a disk."""
        save_json(self, outroot, "raw-funk-maharishi.json")
