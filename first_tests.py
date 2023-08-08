import unittest

from first import merge_overlapping_intervals


class FirstTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_empty_input(self):
        output = merge_overlapping_intervals([])
        self.assertEqual(len(output), 0)

    def test_single_interval(self):
        the_input = [(1, 2)]
        output = merge_overlapping_intervals(the_input)
        self.assertEqual(len(output), 1)
        self.assertEqual(output, the_input)

    def test_two_non_overlapping_intervals(self):
        the_input = [(1, 2), (3, 4)]

        output = merge_overlapping_intervals(the_input)
        self.assertEqual(output, the_input)

    def test_two_overlapping_intervals(self):
        the_input = [(1, 6), (5, 7)]

        output = merge_overlapping_intervals(the_input)
        self.assertEqual(output, [(1, 7)])

    def test_first_example(self):
        the_input = [(1, 2), (3, 5), (6, 8), (9, 10), (4, 7)]
        output = merge_overlapping_intervals(the_input)
        self.assertEqual(len(output), 3)
        self.assertEqual(output, [(1, 2), (3, 8), (9, 10)])
