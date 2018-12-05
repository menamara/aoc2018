import unittest
import day5

class Test_Day5(unittest.TestCase):
    def setUp(self):
        test_input = 'dabAcCaCBAcCcaDA'
        self.polymer = day5.Polymer(test_input)

    def test_reduction(self):
        self.assertEqual(day5.reduce('a'),'a')
        self.assertEqual(day5.reduce('aA'),'')
        self.assertEqual(day5.reduce('aAa'),'a')
        self.assertEqual(day5.reduce('ab'),'ab')
        self.assertEqual(day5.reduce('abBA'),'')
        self.assertEqual(day5.reduce('abAB'),'abAB')
        self.assertEqual(day5.reduce('aabAAB'),'aabAAB')
        self.assertEqual(day5.reduce('aabAAB'),'aabAAB')
        self.assertEqual(day5.reduce('dabAcCaBCBAcCcaDA'),'daCBAcaDA')
    
    def test_polymer(self):
        self.assertEquals(self.polymer.reduced_length(), 10)
