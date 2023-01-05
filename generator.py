import shutil
from pathlib import Path

from lib.gig import Gig
from lib.music_album import MusicAlbum
from lib.person import Person
from lib.raw_funk_maharishi import RawFunkMaharishi
from lib.tools import save_json
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

    save_json(things, "dist", f"{directory}.json")


def make_gigs():
    """Make the `Gigs` data."""
    make_list(Gig, "gigs")


def make_records():
    """Make the `MusicAlbums` data."""
    make_list(MusicAlbum, "records", "datePublished")


def make_venues():
    """Make the `Venues` data."""
    venues = Path("data/venues").glob("**/*.yaml")
    for venue in venues:
        ven = Venue(venue)
        ven.save()


def make_people():
    """Make the `People` data."""
    people = Path("data/people").glob("**/*.yaml")
    for person in people:
        prsn = Person(person)
        prsn.save()


def make_rfm():
    """Make the `RawFunkMaharishi` data."""
    rfm = RawFunkMaharishi()
    rfm.save()


# this could use some tests tbh
if __name__ == "__main__":
    make_dirs()
    make_venues()
    make_people()
    make_gigs()
    make_records()
    make_rfm()
