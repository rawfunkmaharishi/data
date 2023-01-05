from lib.entity import Entity
from lib.raw_funk_maharishi import RawFunkMaharishi


class MusicAlbum(Entity):
    """A record."""

    def refine(self):
        self["@type"] = "MusicAlbum"
        self["name"] = self.data["title"]
        self["identifier"] = self.identifier
        self["byArtist"] = RawFunkMaharishi(with_context=False)
        self["datePublished"] = str(self.data["release_date"])
        self["albumReleaseType"] = self.data["type"]
        self["url"] = f"/records/{self.identifier}"
        self["locationCreated"] = {
            "@type": "Place",
            "name": self.data["location"]["name"],
            "url": self.data["location"]["url"],
        }
        self["genre"] = "Industrial Jazz"

        self["image"] = {
            "@type": "ImageObject",
            "contentUrl": f"/record-covers/{self.data['cover_image']}",
            "name": f"{self.data['title']} cover",
        }

        self["numTracks"] = len(self.data["tracks"])
        self["track"] = list(
            map(lambda x: {"@type": "MusicRecording", "name": x}, self.data["tracks"])
        )

        self["sameAs"] = [
            f"https://www.youtube.com/embed/videoseries?list={self.data['youtube_id']}",
            f"https://open.spotify.com/embed/album/{self.data['spotify_id']}",
        ] + list(map(lambda x: x["url"], self.data["outlets"]))
