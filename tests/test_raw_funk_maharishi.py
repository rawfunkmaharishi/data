import json
from pathlib import Path
from unittest import TestCase

from helpers import clean_house

from generator import make_people
from lib.raw_funk_maharishi import RawFunkMaharishi


class TestRawFunkMaharishi(TestCase):
    """Test RawFunkMaharishi."""

    def setUp(self):
        """Pre-flight shit."""
        clean_house()
        make_people()

    def test_raw_funk_maharishi(self):
        """Test it has the correct data."""
        expected = {
            "@type": "MusicGroup",
            "name": "Raw Funk Maharishi",
            "url": "https://rawfunkmaharishi.uk/",
            "@context": "https://schema.org",
            "member": [
                {
                    "@type": "Person",
                    "image": {
                        "@type": "ImageObject",
                        "contentUrl": "/the-band/joe.png",
                        "name": "Joe",
                    },
                    "knowsAbout": "Guitar",
                    "name": "Joe",
                },
                {
                    "@type": "Person",
                    "image": {
                        "@type": "ImageObject",
                        "contentUrl": "/the-band/matt.png",
                        "name": "Matt",
                    },
                    "knowsAbout": "Bass",
                    "name": "Matt",
                },
                {
                    "@type": "Person",
                    "image": {
                        "@type": "ImageObject",
                        "contentUrl": "/the-band/sam.png",
                        "name": "Sam",
                    },
                    "knowsAbout": "Drums",
                    "name": "Sam",
                    "url": "https://sam.pikesley.org",
                },
            ],
        }

        rfm = RawFunkMaharishi()
        self.assertEqual(rfm, expected)

    def test_saving(self):
        """Test it writes itself to disk."""
        rfm = RawFunkMaharishi()
        rfm.save("tmp")

        actual_path = Path("tmp", "raw-funk-maharishi.json")
        self.assertTrue(actual_path.exists())

        actual = json.loads(actual_path.read_text(encoding="utf-8"))
        self.assertEqual(
            actual,
            {
                "@type": "MusicGroup",
                "name": "Raw Funk Maharishi",
                "url": "https://rawfunkmaharishi.uk/",
                "@context": "https://schema.org",
                "member": [
                    {
                        "@type": "Person",
                        "image": {
                            "@type": "ImageObject",
                            "contentUrl": "/the-band/joe.png",
                            "name": "Joe",
                        },
                        "knowsAbout": "Guitar",
                        "name": "Joe",
                    },
                    {
                        "@type": "Person",
                        "image": {
                            "@type": "ImageObject",
                            "contentUrl": "/the-band/matt.png",
                            "name": "Matt",
                        },
                        "knowsAbout": "Bass",
                        "name": "Matt",
                    },
                    {
                        "@type": "Person",
                        "image": {
                            "@type": "ImageObject",
                            "contentUrl": "/the-band/sam.png",
                            "name": "Sam",
                        },
                        "knowsAbout": "Drums",
                        "name": "Sam",
                        "url": "https://sam.pikesley.org",
                    },
                ],
            },
        )
