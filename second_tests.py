import unittest

from second import area_of_the_water_trapped


class SecondTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_empty_pillars(self):
        output = area_of_the_water_trapped([])
        self.assertEqual(output, 0)

    def test_two_pillars(self):
        output = area_of_the_water_trapped([1, 0, 1])
        self.assertEqual(output, 1)

    def test_6002003_pillars(self):
        output = area_of_the_water_trapped([6, 0, 0, 2, 0, 0, 3])
        self.assertEqual(output, 13)

    def test_challenge_pillars(self):
        output = area_of_the_water_trapped([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3])
        self.assertEqual(output, 48)
