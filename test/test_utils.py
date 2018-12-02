import unittest
from aoc_helpers import dataio

class Test_TestUtils(unittest.TestCase):
    def test_getdata(self):
        self.assertEqual(dataio.get_data(3, 2017), '347991\n')
    def test_loaddata(self):
        self.assertEqual(dataio.load_data(3, 2017), '347991\n')

    def test_geturl(self):
        self.assertEqual(dataio.get_url(2), 'https://adventofcode.com/2018/day/2/input')
        self.assertEqual(dataio.get_url(2, 2017), 'https://adventofcode.com/2017/day/2/input')

    def test_convert_to_int(self):
        self.assertEqual(dataio.convert_to_int('3\n5\n7'), [3,5,7])
        self.assertEqual(dataio.convert_to_int('-3\n+5\n-7'), [-3,5,-7])
        self.assertEqual(dataio.convert_to_int('3\n5\n7\n'), [3,5,7])
        self.assertEqual(dataio.convert_to_int('3\n5\n7\n '), [3,5,7])

    def test_split_data(self):
        self.assertEqual(dataio.split_data('3\n5\n7'), ['3','5','7'])
        self.assertEqual(dataio.split_data('3\n5\n7\n'), ['3','5','7'])
        self.assertEqual(dataio.split_data('3\n5\n7\n '), ['3','5','7'])

if __name__ == '__main__':
    unittest.main()