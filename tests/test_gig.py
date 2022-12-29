from unittest import TestCase

from helpers import clean_house

from lib.gig import Gig
from lib.venue import Venue


class TestGig(TestCase):
    """Test Gig."""

    def setUp(self):
        """Pre-flight shit."""
        clean_house()

    def test_simple_gig(self):
        """Test it has the correct data."""
        # we need this to exist
        venue = Venue("data/venues/luna.yaml")
        venue.save()

        expected = {
            "@context": "https://schema.org",
            "@type": "MusicEvent",
            "performer": {
                "@type": "MusicGroup",
                "name": "Raw Funk Maharishi",
                "sameAs": "https://rawfunkmaharishi.uk/",
            },
            "startDate": "2022-12-15T21:00",
            "location": {
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
                "sameAs": "https://www.lunalivemusic.com/",
            },
            "name": "Raw Funk Maharishi live at Luna Lounge",
            "sameAs": "https://rawfunkmaharishi.uk/gigs/2022/12/15/luna",
            "off-schema": {"name-bits": ["2022", "12", "15", "luna"]},
        }

        gig = Gig("data/gigs/2022-12-15-luna.yaml")
        self.assertEqual(gig, expected)

    def test_gig_with_other_bands(self):
        """Test a gig with `other_bands`."""
        # we need this to exist
        venue = Venue("data/venues/hoxton-underbelly.yaml")
        venue.save()

        expected = {
            "@context": "https://schema.org",
            "@type": "MusicEvent",
            "startDate": "2017-08-14T20:30",
            "location": {
                "@type": "Place",
                "address": {
                    "@type": "PostalAddress",
                    "addressCountry": "United Kingdom",
                    "streetAddress": "11 Hoxton Square, N1 6NU",
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 51.527817,
                    "longitude": -0.08171,
                },
                "name": "Zigfrid von Underbelly",
            },
            "name": "Raw Funk Maharishi live at Zigfrid von Underbelly",
            "sameAs": "https://rawfunkmaharishi.uk/gigs/2017/08/14/hoxton-underbelly",
            "performer": [
                {
                    "@type": "MusicGroup",
                    "name": "Raw Funk Maharishi",
                    "sameAs": "https://rawfunkmaharishi.uk/",
                },
                {
                    "@type": "MusicGroup",
                    "name": "The Curious Incident",
                    "sameAs": "https://www.thecuriousincident.com/",
                },
                {
                    "@type": "MusicGroup",
                    "name": "Dirty Palace",
                    "sameAs": "https://hotvox.co.uk/artists/dirty-palace",
                },
            ],
            "off-schema": {"name-bits": ["2017", "08", "14", "hoxton-underbelly"]},
        }

        gig = Gig("data/gigs/2017-08-14-hoxton-underbelly.yaml")
        self.assertEqual(gig, expected)

    def test_with_fb_event(self):
        """Test it includes the FB Event URL."""
        # we need this to exist
        venue = Venue("data/venues/hoxton-underbelly.yaml")
        venue.save()

        expected = {
            "@context": "https://schema.org",
            "@type": "MusicEvent",
            "startDate": "2015-08-11T21:15",
            "location": {
                "@type": "Place",
                "address": {
                    "@type": "PostalAddress",
                    "addressCountry": "United Kingdom",
                    "streetAddress": "11 Hoxton Square, N1 6NU",
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 51.527817,
                    "longitude": -0.08171,
                },
                "name": "Zigfrid von Underbelly",
            },
            "name": "Raw Funk Maharishi live at Zigfrid von Underbelly",
            "sameAs": [
                "https://rawfunkmaharishi.uk/gigs/2015/08/11/hoxton-underbelly",
                "https://facebook.com/events/674266616008095/",
            ],
            "performer": {
                "@type": "MusicGroup",
                "name": "Raw Funk Maharishi",
                "sameAs": "https://rawfunkmaharishi.uk/",
            },
            "off-schema": {"name-bits": ["2015", "08", "11", "hoxton-underbelly"]},
        }

        gig = Gig("data/gigs/2015-08-11-hoxton-underbelly.yaml")
        self.assertEqual(gig, expected)

    def test_with_price(self):
        """Test it shows ticket prices."""
        # we need this to exist
        venue = Venue("data/venues/the-islington.yaml")
        venue.save()

        expected = {
            "@context": "https://schema.org",
            "@type": "MusicEvent",
            "startDate": "2016-09-04T20:30",
            "location": {
                "@type": "Place",
                "address": {
                    "@type": "PostalAddress",
                    "addressCountry": "United Kingdom",
                    "streetAddress": "1 Tolpuddle St, N1 0XT",
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 51.53442,
                    "longitude": -0.10872,
                },
                "name": "The Islington",
            },
            "name": "Raw Funk Maharishi live at The Islington",
            "sameAs": [
                "https://rawfunkmaharishi.uk/gigs/2016/09/04/the-islington",
                "https://facebook.com/events/1771443439734606/",
            ],
            "performer": {
                "@type": "MusicGroup",
                "name": "Raw Funk Maharishi",
                "sameAs": "https://rawfunkmaharishi.uk/",
            },
            "offers": {"@type": "offer", "price": 6, "priceCurrency": "GBP"},
            "off-schema": {"name-bits": ["2016", "09", "04", "the-islington"]},
        }

        gig = Gig("data/gigs/2016-09-04-the-islington.yaml")
        self.assertEqual(gig, expected)

    def test_with_additional_website(self):
        """Test it generates more sameAs."""
        # we need this to exist
        venue = Venue("data/venues/new-cross-inn.yaml")
        venue.save()

        expected = {
            "@context": "https://schema.org",
            "sameAs": [
                "https://rawfunkmaharishi.uk/gigs/2017/08/18/new-cross-inn",
                "https://facebook.com/events/466457933711377/",
                (
                    "https://www.newcrossinn.com/event/"
                    "friday-funk-project-with-london-beat-club-more/"
                ),
            ],
            "@type": "MusicEvent",
            "startDate": "2017-08-18T20:00",
            "location": {
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
            },
            "name": "Raw Funk Maharishi live at New Cross Inn Hostel",
            "performer": {
                "@type": "MusicGroup",
                "name": "Raw Funk Maharishi",
                "sameAs": "https://rawfunkmaharishi.uk/",
            },
            "offers": {"@type": "offer", "price": 3, "priceCurrency": "GBP"},
            "off-schema": {"name-bits": ["2017", "08", "18", "new-cross-inn"]},
        }

        gig = Gig("data/gigs/2017-08-18-new-cross-inn.yaml")
        self.assertEqual(gig, expected)
