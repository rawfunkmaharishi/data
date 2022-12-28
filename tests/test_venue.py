import json
from pathlib import Path
from unittest import TestCase

from helpers import clean_house

from lib.venue import Venue


class TestVenue(TestCase):
    """Test Venue."""

    def setUp(self):
        """Pre-flight shit."""
        clean_house()

    def test_simple_venue(self):
        """Test it has the correct data."""
        expected = {
            "@context": "https://schema.org",
            "@type": "Place",
            "address": {
                "@type": "PostalAddress",
                "addressCountry": "United Kingdom",
                "streetAddress": "323A New Cross Rd, SE14",
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": 51.475746,
                "longitude": -0.03733,
            },
            "name": "New Cross Inn Hostel",
        }

        venue = Venue("new-cross-inn.yaml")
        self.assertEqual(venue, expected)

    def test_venue_with_website(self):
        """Test it has the correct data."""
        expected = {
            "@context": "https://schema.org",
            "@type": "Place",
            "address": {
                "@type": "PostalAddress",
                "addressCountry": "United Kingdom",
                "streetAddress": "7 Church Lane, E11 1HG",
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": 51.5682837,
                "longitude": 0.0101648,
            },
            "name": "Luna Lounge",
            "sameAs": "//www.lunalivemusic.com/",
        }
        venue = Venue("luna.yaml")
        self.assertEqual(venue, expected)

    def test_saving(self):
        """Test it writes the data."""

        venue = Venue("biddle-brothers.yaml")
        venue.save("tmp")

        actual_path = Path("tmp", "venues", "biddle-brothers.json")
        self.assertTrue(actual_path.exists())

        actual = json.loads(actual_path.read_text(encoding="utf-8"))
        self.assertEqual(
            actual,
            {
                "@context": "https://schema.org",
                "@type": "Place",
                "address": {
                    "@type": "PostalAddress",
                    "addressCountry": "United Kingdom",
                    "streetAddress": "88 Lower Clapton Rd,, E5 0QR",
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 51.5531359,
                    "longitude": -0.0529881,
                },
                "name": "Biddle Brothers",
            },
        )
