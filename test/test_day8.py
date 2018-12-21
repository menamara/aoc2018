import unittest
import day8

class Test_Day5(unittest.TestCase):
    def setUp(self):
        self.test_input = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
            
    def test_matadata_sum(self):
        test_licence = day8.Licence(self.test_input)
        self.assertEqual(test_licence.process_node(),138)
