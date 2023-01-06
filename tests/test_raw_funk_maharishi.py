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
            "review": [
                {
                    "@type": "Review",
                    "reviewBody": "You remind me of Steely Dan without the vocals",
                    "author": "Singer/keyboard player from DWT",
                    "url": "https://twitter.com/dwt_music",
                },
                {
                    "@type": "Review",
                    "reviewBody": "Ambient Jazz-Funk",
                    "author": "Kitty",
                },
                {
                    "@type": "Review",
                    "reviewBody": "Uncommonly good driving music",
                    "author": "@catallaxer on Twitter",
                    "url": "https://twitter.com/catallaxer/status/572134901018959872",
                },
                {
                    "@type": "Review",
                    "reviewBody": (
                        "What Herbie Hancock would sound like if he was a 3-piece band"
                    ),
                    "author": "Guitarist from the Dead Frets",
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
                "review": [
                    {
                        "@type": "Review",
                        "reviewBody": "You remind me of Steely Dan without the vocals",
                        "author": "Singer/keyboard player from DWT",
                        "url": "https://twitter.com/dwt_music",
                    },
                    {
                        "@type": "Review",
                        "reviewBody": "Ambient Jazz-Funk",
                        "author": "Kitty",
                    },
                    {
                        "@type": "Review",
                        "reviewBody": "Uncommonly good driving music",
                        "author": "@catallaxer on Twitter",
                        "url": (
                            "https://twitter.com/catallaxer/status/572134901018959872"
                        ),
                    },
                    {
                        "@type": "Review",
                        "reviewBody": (
                            "What Herbie Hancock would sound like if he was a 3-piece"
                            " band"
                        ),
                        "author": "Guitarist from the Dead Frets",
                    },
                ],
            },
        )
