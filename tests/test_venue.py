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
                "postalCode": "SE14",
                "streetAddress": "323A New Cross Rd",
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": 51.475746,
                "longitude": -0.03733,
            },
            "name": "New Cross Inn Hostel",
        }

        venue = Venue("data/venues/new-cross-inn.yaml")
        self.assertEqual(venue, expected)

    def test_venue_with_website(self):
        """Test it has the correct data."""
        expected = {
            "@context": "https://schema.org",
            "@type": "Place",
            "address": {
                "@type": "PostalAddress",
                "addressCountry": "United Kingdom",
                "postalCode": "E11 1HG",
                "streetAddress": "7 Church Lane",
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": 51.5681154,
                "longitude": 0.0103544,
            },
            "image": {
                "@type": "ImageObject",
                "contentUrl": "/venues/luna.jpg",
                "name": "Luna Lounge",
            },
            "name": "Luna Lounge",
            "url": "https://www.lunalivemusic.com/",
        }
        venue = Venue("data/venues/luna.yaml")
        self.assertEqual(venue, expected)

    def test_saving(self):
        """Test it writes the data."""
        venue = Venue("data/venues/biddle-brothers.yaml")
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
                    "postalCode": "E5 0QR",
                    "streetAddress": "88 Lower Clapton Rd",
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 51.5531359,
                    "longitude": -0.0529881,
                },
                "name": "Biddle Brothers",
            },
        )
