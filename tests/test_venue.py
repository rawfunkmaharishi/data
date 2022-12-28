from unittest import TestCase

from lib.venue import Venue


class TestVenue(TestCase):
    """Test Venue."""

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
