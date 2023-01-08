from fixtures.band.member import member
from fixtures.band.review import review
from fixtures.context import context

band = {
    "@type": "MusicGroup",
    "name": "Raw Funk Maharishi",
    "url": "https://rawfunkmaharishi.uk/",
    "member": member,
    "review": review,
    "aggregateRating": {"@type": "AggregateRating", "reviewCount": 4, "ratingValue": 5},
}

band_with_context = band | context
