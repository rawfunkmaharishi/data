import json
import shutil
from pathlib import Path

import yaml

outdir = Path("dist/gigs")
if outdir.exists():
    shutil.rmtree(str(outdir))

Path(outdir).mkdir(exist_ok=True, parents=True)

gigs = Path("data/gigs").glob("**/*.yaml")

for gig in gigs:
    data = yaml.safe_load(gig.read_text())
    ld = {
        "@context": "http://schema.org",
        "@type": "MusicEvent",
        "performer": {
            "@type": "MusicGroup",
            "name": "Raw Funk Maharishi",
            "sameAs": "//rawfunkmaharishi.uk/",
        },
    }

    datestamp = f'{"-".join(str(gig).split("/")[2:5])}T{data["time"]}'
    ld["startDate"] = datestamp

    location = json.loads(Path("dist", "venues", f"{data['venue']}.json").read_text())
    del location["@context"]
    ld["location"] = location
    ld["name"] = f"Raw Funk Maharishi live at {location['name']}"

    outpath = Path(str(gig).replace("data", "dist")).parent
    outpath.mkdir(exist_ok=True, parents=True)
    Path(outpath, f"{gig.stem}.json").write_text(json.dumps(ld, sort_keys=True))

    # Path(outdir, f"{gig.stem}.json").write_text(json.dumps(ld, sort_keys=True))

        # "offers": {
        #     "@type": "offer",
        #     "availability": "Not relevant",
        #     "price": "0",
        #     "priceCurrency": "GBP",
        #     "url": "//www.lunalivemusic.com/",
        # },
