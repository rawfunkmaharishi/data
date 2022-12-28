# import json
# import shutil
# from pathlib import Path

# import yaml

# gigs = Path("data/gigs").glob("**/*.yaml")
# all_gigs = []

# conf = yaml.safe_load(Path("conf.yaml").read_text())

# for gig in gigs:
#     data = yaml.safe_load(gig.read_text())
#     ld = {
#         "@context": "http://schema.org",
#         "@type": "MusicEvent",
#         "performer": {
#             "@type": "MusicGroup",
#             "name": "Raw Funk Maharishi",
#             "sameAs": "//rawfunkmaharishi.uk/",
#         },
#     }

#     date = "-".join(str(gig).split("/")[2:5])
#     datestamp = f'{date}T{data["time"]}'
#     ld["startDate"] = datestamp

#     location = json.loads(Path("dist", "venues", f"{data['venue']}.json").read_text())
#     del location["@context"]
#     ld["location"] = location
#     ld["name"] = f"Raw Funk Maharishi live at {location['name']}"

#     urlpath = Path(str(gig).replace("data", "dist")).parent
#     url = f"{str(urlpath).replace('dist', conf['webserver'])}/{gig.stem}"
#     ld["sameAs"] = url

#     all_gigs.append(ld)

# Path("dist", "gigs.json").write_text((json.dumps(all_gigs)))

# # "offers": {
# #     "@type": "offer",
# #     "availability": "Not relevant",
# #     "price": "0",
# #     "priceCurrency": "GBP",
# #     "url": "//www.lunalivemusic.com/",
# # },
