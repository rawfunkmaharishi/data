# import json
# import shutil
# from pathlib import Path

# import yaml

# outdir = Path("dist/venues")
# if outdir.exists():
#     shutil.rmtree(str(outdir))

# Path(outdir).mkdir(exist_ok=True, parents=True)

# venues = Path("data/venues").glob("**/*.yaml")

# for venue in venues:
#     data = yaml.safe_load(venue.read_text())

#     ld = {
#         "@context": "https://schema.org",
#         "@type": "Place",
#         "address": {
#             "@type": "PostalAddress",
#             "addressCountry": "United Kingdom",
#             "streetAddress": f"{data['address']}, {data['postcode']}",
#         },
#         "geo": {
#             "@type": "GeoCoordinates",
#             "latitude": data["latitude"],
#             "longitude": data["longitude"],
#         },
#         "name": data["name"],
#     }
#     if "website" in data:
#         ld["sameAs"] = data["website"]

#     Path(outdir, f"{venue.stem}.json").write_text(json.dumps(ld, sort_keys=True))
