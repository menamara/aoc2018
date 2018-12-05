import unittest
import day5

class Test_Day5(unittest.TestCase):
    def setUp(self):
        test_input = 'dabAcCaCBAcCcaDA'
        self.polymer = day5.Polymer(test_input)
    
    def test_delete_char(self):
       self.assertEqual(day5.delete_char('dabAcCaCBAcCcaDA','a'),'dbcCCBcCcD') 
       self.assertEqual(day5.delete_char('dabAcCaCBAcCcaDA','b'),'daAcCaCAcCcaDA') 
       self.assertEqual(day5.delete_char('dabAcCaCBAcCcaDA','c'),'dabAaBAaDA') 
       self.assertEqual(day5.delete_char('dabAcCaCBAcCcaDA','d'),'abAcCaCBAcCcaA') 
    
    def test_min_len(self):
        self.assertEqual(self.polymer.reduced_length_with_broken_unit('a'),6)
        self.assertEqual(self.polymer.reduced_length_with_broken_unit('b'),8)
        self.assertEqual(self.polymer.reduced_length_with_broken_unit('c'),4)
        self.assertEqual(self.polymer.reduced_length_with_broken_unit('d'),6)
        self.assertEqual(day5.find_shortest(self.polymer), 4) 

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
