import json
import shutil
from pathlib import Path

from lib.gig import Gig
from lib.venue import Venue


def make_dirs():
    """Make the output dirs."""
    outdir = Path("dist/venues")
    if outdir.exists():
        shutil.rmtree(str(outdir))

    Path(outdir).mkdir(exist_ok=True, parents=True)


def make_venues():
    """Make the `Venues` data."""
    venues = Path("data/venues").glob("**/*.yaml")
    for venue in venues:
        ven = Venue(venue)
        ven.save()


def make_gigs():
    """Make the `Gigs` data."""
    gigs = list(map(Gig, Path("data/gigs").glob("**/*.yaml")))
    Path("dist/gigs.json").write_text(json.dumps(gigs), encoding="utf-8")


if __name__ == "__main__":
    make_dirs()
    make_venues()
    make_gigs()
