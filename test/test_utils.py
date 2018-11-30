import unittest
from utils import dataio

class Test_TestUtils(unittest.TestCase):
    def test_getdata(self):
        self.assertEqual(dataio.get_data(3, 2017), '347991\n')
    def test_loaddata(self):
        self.assertEqual(dataio.load_data(3, 2017), '347991\n')

    def test_geturl(self):
        self.assertEqual(dataio.get_url(2), 'https://adventofcode.com/2018/day/2/input')
        self.assertEqual(dataio.get_url(2, 2017), 'https://adventofcode.com/2017/day/2/input')

if __name__ == '__main__':
    unittest.main()