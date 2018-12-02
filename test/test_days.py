import unittest
import day1, day2

class Test_TestDays(unittest.TestCase):

    def test_day2_chekcsum(self):
        test_input = [ 'abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
        self.assertEqual(day2.checksum(test_input), 12)

    def test_day1_1(self):
        self.assertEqual(day1.add([+1, -2, +3, +1]), 3)
        self.assertEqual(day1.add([+1, +1, +1]), 3)
        self.assertEqual(day1.add([+1, +1, -2]), 0)
        self.assertEqual(day1.add([-1, -2, -3]), -6)
                
    def test_day1_2(self):
        self.assertEqual(day1.find_loop([+1, -1]), 0)
        self.assertEqual(day1.find_loop([+3, +3, +4, -2, -4]), 10)
        self.assertEqual(day1.find_loop([-6, +3, +8, +5, -6]), 5)
        self.assertEqual(day1.find_loop([+7, +7, -2, -7, -4]), 14)