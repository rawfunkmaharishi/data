import json
import shutil
from pathlib import Path

from lib.gig import Gig
from lib.music_album import MusicAlbum
from lib.person import Person
from lib.venue import Venue


def make_dirs():
    """Make the output dirs."""
    outdir = Path("dist/venues")
    if outdir.exists():
        shutil.rmtree(str(outdir))

    Path(outdir).mkdir(exist_ok=True, parents=True)


def make_list(klass, directory, sort_key=None):
    """Make a list of things."""
    things = list(map(klass, Path("data", directory).glob("**/*.yaml")))
    if sort_key:
        things.sort(key=lambda x: x[sort_key])
    Path("dist", f"{directory}.json").write_text(json.dumps(things), encoding="utf-8")


def make_gigs():
    """Make the `Gigs` data."""
    make_list(Gig, "gigs")


def make_records():
    """Make the `MusicAlbums` data."""
    make_list(MusicAlbum, "records", "datePublished")


def make_people():
    """Make the `People` data."""
    make_list(Person, "people")


def make_venues():
    """Make the `Venues` data."""
    venues = Path("data/venues").glob("**/*.yaml")
    for venue in venues:
        ven = Venue(venue)
        ven.save()


# this could use some tests tbh
if __name__ == "__main__":
    make_dirs()
    make_venues()
    make_gigs()
    make_records()
    make_people()
