from unittest import TestCase

from fixtures.band.band import band
from helpers import clean_house

from generator import make_venues
from lib.gig import Gig


class TestGig(TestCase):
    """Test Gig."""

    def setUp(self):
        """Pre-flight shit."""
        clean_house()
        make_venues()

    def test_simple_gig(self):
        """Test it has the correct data."""
        expected = {
            "@context": "https://schema.org",
            "@type": "MusicEvent",
            "startDate": "2022-12-15T21:00",
            "location": {
                "@type": "Place",
                "address": {
                    "@type": "PostalAddress",
                    "addressCountry": "United Kingdom",
                    "postalCode": "E11 1HG",
                    "streetAddress": "7 Church Lane",
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 51.5682837,
                    "longitude": 0.0101648,
                },
                "name": "Luna Lounge",
                "url": "https://www.lunalivemusic.com/",
            },
            "name": "Raw Funk Maharishi live at Luna Lounge",
            "url": "/gigs/2022/12/15/luna",
            "performer": band,
            "isAccessibleForFree": True,
            "recordedIn": {
                "@type": "VideoObject",
                "@id": "https://www.youtube.com/watch?v=JYP6eA5yqc4",
                "name": "Raw Funk Maharishi live at Luna Lounge",
                "description": "Raw Funk Maharishi live at Luna Lounge",
                "uploadDate": "2022-12-15",
                "thumbnailUrl": "https://img.youtube.com/vi/JYP6eA5yqc4/default.jpg",
                "embedUrl": "https://www.youtube.com/embed/JYP6eA5yqc4",
            },
        }

        gig = Gig("data/gigs/2022-12-15-luna.yaml")
        self.assertEqual(gig, expected)

    def test_gig_with_other_bands(self):
        """Test a gig with `other_bands`."""
        expected = {
            "@context": "https://schema.org",
            "@type": "MusicEvent",
            "startDate": "2017-08-14T20:30",
            "location": {
                "@type": "Place",
                "address": {
                    "@type": "PostalAddress",
                    "addressCountry": "United Kingdom",
                    "postalCode": "N1 6NU",
                    "streetAddress": "11 Hoxton Square",
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 51.527817,
                    "longitude": -0.08171,
                },
                "name": "Zigfrid von Underbelly",
            },
            "name": "Raw Funk Maharishi live at Zigfrid von Underbelly",
            "url": "/gigs/2017/08/14/hoxton-underbelly",
            "performer": [
                band,
                {
                    "@type": "MusicGroup",
                    "name": "The Curious Incident",
                    "url": "https://www.thecuriousincident.com/",
                },
                {
                    "@type": "MusicGroup",
                    "name": "Dirty Palace",
                    "url": "https://hotvox.co.uk/artists/dirty-palace",
                },
            ],
            "isAccessibleForFree": True,
        }

        gig = Gig("data/gigs/2017-08-14-hoxton-underbelly.yaml")
        self.assertEqual(gig, expected)

    def test_with_fb_event(self):
        """Test it includes the FB Event URL."""
        expected = {
            "@context": "https://schema.org",
            "@type": "MusicEvent",
            "startDate": "2015-08-11T21:15",
            "location": {
                "@type": "Place",
                "address": {
                    "@type": "PostalAddress",
                    "addressCountry": "United Kingdom",
                    "postalCode": "N1 6NU",
                    "streetAddress": "11 Hoxton Square",
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 51.527817,
                    "longitude": -0.08171,
                },
                "name": "Zigfrid von Underbelly",
            },
            "name": "Raw Funk Maharishi live at Zigfrid von Underbelly",
            "url": "/gigs/2015/08/11/hoxton-underbelly",
            "sameAs": ["https://facebook.com/events/674266616008095/"],
            "performer": band,
            "isAccessibleForFree": True,
        }

        gig = Gig("data/gigs/2015-08-11-hoxton-underbelly.yaml")
        self.assertEqual(gig, expected)

    def test_with_price(self):
        """Test it shows ticket prices."""
        expected = {
            "@context": "https://schema.org",
            "@type": "MusicEvent",
            "startDate": "2016-09-04T20:30",
            "location": {
                "@type": "Place",
                "address": {
                    "@type": "PostalAddress",
                    "addressCountry": "United Kingdom",
                    "postalCode": "N1 0XT",
                    "streetAddress": "1 Tolpuddle St",
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 51.53442,
                    "longitude": -0.10872,
                },
                "name": "The Islington",
            },
            "name": "Raw Funk Maharishi live at The Islington",
            "url": "/gigs/2016/09/04/the-islington",
            "sameAs": ["https://facebook.com/events/1771443439734606/"],
            "performer": band,
            "offers": {"@type": "offer", "price": 6, "priceCurrency": "GBP"},
        }

        gig = Gig("data/gigs/2016-09-04-the-islington.yaml")
        self.assertEqual(gig, expected)

    def test_with_additional_website(self):
        """Test it generates more sameAs."""
        expected = {
            "@context": "https://schema.org",
            "url": "/gigs/2017/08/18/new-cross-inn",
            "@type": "MusicEvent",
            "startDate": "2017-08-18T20:00",
            "location": {
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
            },
            "name": "Raw Funk Maharishi live at New Cross Inn Hostel",
            "sameAs": [
                "https://facebook.com/events/466457933711377/",
                (
                    "https://www.newcrossinn.com/event/"
                    "friday-funk-project-with-london-beat-club-more/"
                ),
            ],
            "performer": band,
            "offers": {"@type": "offer", "price": 3, "priceCurrency": "GBP"},
        }

        gig = Gig("data/gigs/2017-08-18-new-cross-inn.yaml")
        self.assertEqual(gig, expected)

    def test_with_promoter(self):
        """Test a gig with a `promoter`."""
        expected = {
            "@context": "https://schema.org",
            "@type": "MusicEvent",
            "startDate": "2019-10-24T21:20",
            "location": {
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
            "name": "Raw Funk Maharishi live at Biddle Brothers",
            "url": "/gigs/2019/10/24/sad-house-daddy",
            "sameAs": ["https://facebook.com/events/577151796358191/"],
            "performer": [
                band,
                {
                    "@type": "MusicGroup",
                    "name": "JJT Duo",
                    "url": "https://www.youtube.com/channel/UCPjiLQ-VzffhilciNow1QWQ",
                },
                {
                    "@type": "MusicGroup",
                    "name": "Portacle",
                    "url": "https://portacle.bandcamp.com/",
                },
            ],
            "isAccessibleForFree": True,
            "organizer": {"@type": "Organization", "name": "Sad House Daddy"},
        }

        gig = Gig("data/gigs/2019-10-24-sad-house-daddy.yaml")
        self.assertEqual(gig, expected)
