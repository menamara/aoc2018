import unittest
import day1, day2, day3

class Test_TestDays(unittest.TestCase):

    def test_day3_special_area(self):
        test_area_list = day3.Area_List(['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2'])
        self.assertEqual(test_area_list.find_unoverlapping_area(), 3)

    def test_day3_test_area_overlap(self):
        test_area_list = day3.Area_List(['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2'])
        self.assertEqual(test_area_list.area_list[0].has_overlap(test_area_list.area_list[1]), True)
        self.assertEqual(test_area_list.area_list[0].has_overlap(test_area_list.area_list[2]), False)
        self.assertEqual(test_area_list.area_list[1].has_overlap(test_area_list.area_list[2]), False)
    
    def test_day3_Area_Class(self):
        test_area = day3.Area('#1 @ 493,113: 12x14')
        self.assertEqual(test_area.id, 1)
        self.assertEqual(test_area.x, 493 )
        self.assertEqual(test_area.y, 113 )
        self.assertEqual(test_area.dx, 12)
        self.assertEqual(test_area.dy, 14)
        self.assertEqual(test_area.area, 168)

    def test_day3_Area_List_Class(self):
        test_area_list = day3.Area_List(['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2'])
        self.assertEqual(test_area_list.count_overlap_linear(), 4)
    
    def test_day2_find_matching(self):
        test_input = [ 'abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
        self.assertEqual(day2.find_matching(test_input), 'fgij')

    def test_day2_is_match(self):
        self.assertEqual(day2.is_match('fghij', 'fguij'), 'fgij')
        self.assertEqual(day2.is_match('fxhij', 'fguij'), '')

    def test_day2_checksum(self):
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