import json
from pathlib import Path
from unittest import TestCase

from fixtures.band.band import band_with_context
from helpers import clean_house

from generator import make_people
from lib.raw_funk_maharishi import RawFunkMaharishi


class TestRawFunkMaharishi(TestCase):
    """Test RawFunkMaharishi."""

    def setUp(self):
        """Pre-flight shit."""
        clean_house()
        make_people()

    def test_raw_funk_maharishi(self):
        """Test it has the correct data."""

        rfm = RawFunkMaharishi()
        self.assertEqual(rfm, band_with_context)

    def test_saving(self):
        """Test it writes itself to disk."""
        rfm = RawFunkMaharishi()
        rfm.save("tmp")

        actual_path = Path("tmp", "raw-funk-maharishi.json")
        self.assertTrue(actual_path.exists())

        actual = json.loads(actual_path.read_text(encoding="utf-8"))
        self.assertEqual(actual, band_with_context)
