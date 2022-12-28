import json
import shutil
from pathlib import Path

import yaml

outdir = Path("dist/gigs")
if outdir.exists():
    shutil.rmtree(str(outdir))

Path(outdir).mkdir(exist_ok=True, parents=True)

gigs = Path("data/gigs").glob("**/*.yaml")
all_gigs = []

conf = yaml.safe_load(Path("conf.yaml").read_text())

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

    url = f"{str(outpath).replace('dist', conf['api-server'])}/{gig.stem}.json"
    all_gigs.append(url)

Path("dist", "gigs.json").write_text((json.dumps(all_gigs)))
        # "offers": {
        #     "@type": "offer",
        #     "availability": "Not relevant",
        #     "price": "0",
        #     "priceCurrency": "GBP",
        #     "url": "//www.lunalivemusic.com/",
        # },
