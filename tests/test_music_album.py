from unittest import TestCase

from helpers import clean_house

from lib.music_album import MusicAlbum


class TestMusicAlbum(TestCase):
    """Test MusicAlbum."""

    def setUp(self):
        """Pre-flight shit."""
        clean_house()

    def test_album(self):
        """Test it has the correct data."""
        expected = {
            "@context": "https://schema.org",
            "@type": "MusicAlbum",
            "name": "Flux",
            "identifier": "flux",
            "byArtist": {
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
            "datePublished": "2018-04-28",
            "albumReleaseType": "EP",
            "url": "/records/flux",
            "locationCreated": {
                "@type": "Place",
                "name": "Wax Studios",
                "url": "https://waxrecordingstudio.info/",
            },
            "genre": "Industrial Jazz",
            "image": {
                "@type": "ImageObject",
                "contentUrl": "/record-covers/flux.jpg",
                "name": "Flux cover",
            },
            "numTracks": 7,
            "track": [
                {"@type": "MusicRecording", "name": "Boot"},
                {"@type": "MusicRecording", "name": "Cone Mill"},
                {"@type": "MusicRecording", "name": "Flux"},
                {"@type": "MusicRecording", "name": "Noble"},
                {"@type": "MusicRecording", "name": "Tree Deliveries"},
                {"@type": "MusicRecording", "name": "Ceramic Dragon"},
                {"@type": "MusicRecording", "name": "Fade Zero"},
            ],
            "sameAs": [
                (
                    "https://www.youtube.com/embed/videoseries?"
                    "list=PLuPLM2FI60-OlLoRt_FsbRFmi6v5wXKm9"
                ),
                "https://open.spotify.com/embed/album/0V93nqs6M6JNtHE0OJvvgY",
                "https://music.apple.com/us/album/flux/1372617971",
                "https://www.amazon.co.uk/Flux-Raw-Funk-Maharishi/dp/B07CG3PG84/",
            ],
        }

        album = MusicAlbum("data/records/flux.yaml")
        self.assertEqual(album, expected)
