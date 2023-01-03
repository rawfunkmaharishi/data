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
            "identifier": "flux",
            "name": "Flux",
            "byArtist": {"@type": "MusicGroup", "name": "Raw Funk Maharishi"},
            "datePublished": "2018-04-28",
            "albumReleaseType": "EP",
            "url": "/records/flux",
            "locationCreated": {
                "@type": "Place",
                "name": "Wax Studios",
                "sameAs": "https://waxrecordingstudio.info/",
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
            "offSchema": {
                "YouTubeURL": (
                    "https://www.youtube.com/embed/videoseries?"
                    "list=PLuPLM2FI60-OlLoRt_FsbRFmi6v5wXKm9"
                ),
                "SpotifyURL": (
                    "https://open.spotify.com/embed/album/0V93nqs6M6JNtHE0OJvvgY"
                ),
                "otherOutlets": [
                    {
                        "name": "apple music",
                        "url": "https://music.apple.com/us/album/flux/1372617971",
                    },
                    {
                        "name": "amazon",
                        "url": (
                            "https://www.amazon.co.uk/"
                            "Flux-Raw-Funk-Maharishi/dp/B07CG3PG84/"
                        ),
                    },
                ],
            },
            "sameAs": [
                "https://rawfunkmaharishi.uk//records/flux",
                (
                    "https://www.youtube.com/embed/videoseries"
                    "?list=PLuPLM2FI60-OlLoRt_FsbRFmi6v5wXKm9"
                ),
                "https://open.spotify.com/embed/album/0V93nqs6M6JNtHE0OJvvgY",
                "https://music.apple.com/us/album/flux/1372617971",
                "https://www.amazon.co.uk/Flux-Raw-Funk-Maharishi/dp/B07CG3PG84/",
            ],
        }

        album = MusicAlbum("data/records/flux.yaml")
        self.assertEqual(album, expected)
