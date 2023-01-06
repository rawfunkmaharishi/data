from unittest import TestCase

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
                    "streetAddress": "7 Church Lane, E11 1HG",
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
            "performer": {
                "@type": "MusicGroup",
                "name": "Raw Funk Maharishi",
                "url": "https://rawfunkmaharishi.uk/",
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
                        "author": {
                            "type": "Person",
                            "name": "Singer/keyboard player from DWT",
                        },
                        "url": "https://twitter.com/dwt_music",
                    },
                    {
                        "@type": "Review",
                        "reviewBody": "Ambient Jazz-Funk",
                        "author": {"type": "Person", "name": "Kitty"},
                    },
                    {
                        "@type": "Review",
                        "reviewBody": "Uncommonly good driving music",
                        "author": {"type": "Person", "name": "@catallaxer on Twitter"},
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
                        "author": {
                            "type": "Person",
                            "name": "Guitarist from the Dead Frets",
                        },
                    },
                ],
                "aggregateRating": (
                    {"@type": "AggregateRating", "reviewCount": 4, "ratingValue": 5},
                ),
            },
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
            "url": "/gigs/2017/08/14/hoxton-underbelly",
            "performer": [
                {
                    "@type": "MusicGroup",
                    "name": "Raw Funk Maharishi",
                    "url": "https://rawfunkmaharishi.uk/",
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
                            "reviewBody": (
                                "You remind me of Steely Dan without the vocals"
                            ),
                            "author": {
                                "type": "Person",
                                "name": "Singer/keyboard player from DWT",
                            },
                            "url": "https://twitter.com/dwt_music",
                        },
                        {
                            "@type": "Review",
                            "reviewBody": "Ambient Jazz-Funk",
                            "author": {"type": "Person", "name": "Kitty"},
                        },
                        {
                            "@type": "Review",
                            "reviewBody": "Uncommonly good driving music",
                            "author": {
                                "type": "Person",
                                "name": "@catallaxer on Twitter",
                            },
                            "url": "https://twitter.com/catallaxer/status/572134901018959872",
                        },
                        {
                            "@type": "Review",
                            "reviewBody": (
                                "What Herbie Hancock would sound like if he was a"
                                " 3-piece band"
                            ),
                            "author": {
                                "type": "Person",
                                "name": "Guitarist from the Dead Frets",
                            },
                        },
                    ],
                    "aggregateRating": (
                        {
                            "@type": "AggregateRating",
                            "reviewCount": 4,
                            "ratingValue": 5,
                        },
                    ),
                },
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
            "url": "/gigs/2015/08/11/hoxton-underbelly",
            "sameAs": ["https://facebook.com/events/674266616008095/"],
            "performer": {
                "@type": "MusicGroup",
                "name": "Raw Funk Maharishi",
                "url": "https://rawfunkmaharishi.uk/",
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
                        "author": {
                            "type": "Person",
                            "name": "Singer/keyboard player from DWT",
                        },
                        "url": "https://twitter.com/dwt_music",
                    },
                    {
                        "@type": "Review",
                        "reviewBody": "Ambient Jazz-Funk",
                        "author": {"type": "Person", "name": "Kitty"},
                    },
                    {
                        "@type": "Review",
                        "reviewBody": "Uncommonly good driving music",
                        "author": {"type": "Person", "name": "@catallaxer on Twitter"},
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
                        "author": {
                            "type": "Person",
                            "name": "Guitarist from the Dead Frets",
                        },
                    },
                ],
                "aggregateRating": (
                    {"@type": "AggregateRating", "reviewCount": 4, "ratingValue": 5},
                ),
            },
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
            "url": "/gigs/2016/09/04/the-islington",
            "sameAs": ["https://facebook.com/events/1771443439734606/"],
            "performer": {
                "@type": "MusicGroup",
                "name": "Raw Funk Maharishi",
                "url": "https://rawfunkmaharishi.uk/",
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
                        "author": {
                            "type": "Person",
                            "name": "Singer/keyboard player from DWT",
                        },
                        "url": "https://twitter.com/dwt_music",
                    },
                    {
                        "@type": "Review",
                        "reviewBody": "Ambient Jazz-Funk",
                        "author": {"type": "Person", "name": "Kitty"},
                    },
                    {
                        "@type": "Review",
                        "reviewBody": "Uncommonly good driving music",
                        "author": {"type": "Person", "name": "@catallaxer on Twitter"},
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
                        "author": {
                            "type": "Person",
                            "name": "Guitarist from the Dead Frets",
                        },
                    },
                ],
                "aggregateRating": (
                    {"@type": "AggregateRating", "reviewCount": 4, "ratingValue": 5},
                ),
            },
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
            "sameAs": [
                "https://facebook.com/events/466457933711377/",
                (
                    "https://www.newcrossinn.com/event/"
                    "friday-funk-project-with-london-beat-club-more/"
                ),
            ],
            "performer": {
                "@type": "MusicGroup",
                "name": "Raw Funk Maharishi",
                "url": "https://rawfunkmaharishi.uk/",
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
                        "author": {
                            "type": "Person",
                            "name": "Singer/keyboard player from DWT",
                        },
                        "url": "https://twitter.com/dwt_music",
                    },
                    {
                        "@type": "Review",
                        "reviewBody": "Ambient Jazz-Funk",
                        "author": {"type": "Person", "name": "Kitty"},
                    },
                    {
                        "@type": "Review",
                        "reviewBody": "Uncommonly good driving music",
                        "author": {"type": "Person", "name": "@catallaxer on Twitter"},
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
                        "author": {
                            "type": "Person",
                            "name": "Guitarist from the Dead Frets",
                        },
                    },
                ],
                "aggregateRating": (
                    {"@type": "AggregateRating", "reviewCount": 4, "ratingValue": 5},
                ),
            },
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
                    "streetAddress": "88 Lower Clapton Rd,, E5 0QR",
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
                {
                    "@type": "MusicGroup",
                    "name": "Raw Funk Maharishi",
                    "url": "https://rawfunkmaharishi.uk/",
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
                            "reviewBody": (
                                "You remind me of Steely Dan without the vocals"
                            ),
                            "author": {
                                "type": "Person",
                                "name": "Singer/keyboard player from DWT",
                            },
                            "url": "https://twitter.com/dwt_music",
                        },
                        {
                            "@type": "Review",
                            "reviewBody": "Ambient Jazz-Funk",
                            "author": {"type": "Person", "name": "Kitty"},
                        },
                        {
                            "@type": "Review",
                            "reviewBody": "Uncommonly good driving music",
                            "author": {
                                "type": "Person",
                                "name": "@catallaxer on Twitter",
                            },
                            "url": "https://twitter.com/catallaxer/status/572134901018959872",
                        },
                        {
                            "@type": "Review",
                            "reviewBody": (
                                "What Herbie Hancock would sound like if he was a"
                                " 3-piece band"
                            ),
                            "author": {
                                "type": "Person",
                                "name": "Guitarist from the Dead Frets",
                            },
                        },
                    ],
                    "aggregateRating": (
                        {
                            "@type": "AggregateRating",
                            "reviewCount": 4,
                            "ratingValue": 5,
                        },
                    ),
                },
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
