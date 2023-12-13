import unittest as ut
from day1 import extract_coords

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
        self.assertEqual(
            extract_coords("two1nine"), 29
        )
        self.assertEqual(
            extract_coords("eightwothree"), 83
        )
        self.assertEqual(
            extract_coords("abcone2threexyz"), 13
        )
        self.assertEqual(
            extract_coords("xtwone3four"), 24
        )
        self.assertEqual(
            extract_coords("4nineeightseven2"), 42
        )
        self.assertEqual(
            extract_coords("zoneight234"), 14
        )
        self.assertEqual(
            extract_coords("7pqrstsixteen"), 76
        )
        self.assertEqual(
            extract_coords("one"), 11
        )

        self.assertEqual(
            extract_coords("one6xzxmmjpone7ngdlvvhljmhztlbsgxthree"), 13
        )











