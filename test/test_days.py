import unittest
from sources import day1

class Test_TestDays(unittest.TestCase):
    def test_day1_1(self):
        self.assertEqual(day1.add([+1, -2, +3, +1]), 3)
        self.assertEqual(day1.add([+1, +1, +1]), 3)
        self.assertEqual(day1.add([+1, +1, -2]), 0)
        self.assertEqual(day1.add([-1, -2, -3]), -6)