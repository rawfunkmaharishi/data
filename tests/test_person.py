from unittest import TestCase

from helpers import clean_house

from lib.person import Person


class TestPerson(TestCase):
    """Test Person."""

    def setUp(self):
        """Pre-flight shit."""
        clean_house()

    def test_person(self):
        """Test it has the correct data."""
        expected = {
            "@context": "https://schema.org",
            "@type": "Person",
            "name": "Sam",
            "knowsAbout": "Drums",
            "image": {
                "@type": "ImageObject",
                "contentUrl": "/the-band/sam.png",
                "name": "Sam",
            },
            "url": "https://sam.pikesley.org",
        }

        person = Person("data/people/sam.yaml")
        self.assertEqual(person, expected)
