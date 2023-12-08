import unittest as ut
from day1 import extract_coords, sum_coords


class TestDay1(ut.TestCase):

    def test_extract_coords(self):
        self.assertEqual(
            extract_coords("1abc2"), 12
        )
        self.assertEqual(
            extract_coords("pqr3stu8vwx"), 38
        )
        self.assertEqual(
            extract_coords("a1b2c3d4e5f"), 15
        )
        self.assertEqual(
            extract_coords("treb7uchet"), 77
        )



