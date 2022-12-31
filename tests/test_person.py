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
            "image": "https://rawfunkmaharishi.uk/the-band/sam.png",
            "sameAs": "https://sam.pikesley.org",
            "offSchema": {"image": "sam.png"},
        }

        person = Person("data/people/sam.yaml")
        self.assertEqual(person, expected)
