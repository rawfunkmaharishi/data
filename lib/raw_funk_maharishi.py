from pathlib import Path

import yaml

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
                sorted(list(Path("dist/people").glob("*.json"))),
            )
        )

        self["review"] = self.reviews
        self["aggregateRating"] = {
            "@type": "AggregateRating",
            "reviewCount": len(self["review"]),
            "ratingValue": 5,
        }

    def save(self, outroot="dist"):
        """Write ourselves to a disk."""
        save_json(self, outroot, "raw-funk-maharishi.json")

    @property
    def reviews(self):
        """Gather reviews of the band."""
        results = []

        for review in yaml.safe_load(
            Path("data/reviews.yaml").read_text(encoding="utf-8")
        ):
            rvw = {
                "@type": "Review",
                "reviewBody": review["quote"],
                "author": {
                    "type": "Person",
                    "name": review["source"],
                },
            }
            if "url" in review:
                rvw["url"] = review["url"]

            results.append(rvw)

        return results
