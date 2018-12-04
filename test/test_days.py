import unittest
import day1, day2, day3, day4

class Test_Day4(unittest.TestCase):
    def setUp(self):
        test_input = [
            '[1518-11-01 00:00] Guard #10 begins shift',
            '[1518-11-01 00:05] falls asleep',
            '[1518-11-01 00:25] wakes up',
            '[1518-11-01 00:30] falls asleep',
            '[1518-11-01 00:55] wakes up',
            '[1518-11-01 23:58] Guard #99 begins shift',
            '[1518-11-02 00:40] falls asleep',
            '[1518-11-02 00:50] wakes up',
            '[1518-11-03 00:05] Guard #10 begins shift',
            '[1518-11-03 00:24] falls asleep',
            '[1518-11-03 00:29] wakes up',
            '[1518-11-04 00:02] Guard #99 begins shift',
            '[1518-11-04 00:36] falls asleep',
            '[1518-11-04 00:46] wakes up',
            '[1518-11-05 00:03] Guard #99 begins shift',
            '[1518-11-05 00:45] falls asleep',
            '[1518-11-05 00:55] wakes up']
        self.entries = []
        for line in test_input:
            self.entries.append(day4.Log_Entry(line))
        self.list_of_days = day4.compile_list_of_days(test_input)
        self.list_of_guards = day4.assign_days_to_guards(test_input)
        self.longest_sleeper = day4.find_longest_sleeper(test_input)
        self.most_consistent_sleeper = day4.find_most_consistent_sleeper(test_input)

    def test_strategy2(self):
        self.assertEquals(self.most_consistent_sleeper, 4455)

    def test_guards(self):
        self.assertEqual('99' in self.list_of_guards, True)
        self.assertEqual('10' in self.list_of_guards, True)
        self.assertEqual(self.list_of_guards['99'].count_asleep_minutes(), 30)
        self.assertEqual(self.list_of_guards['10'].count_asleep_minutes(), 50)
        self.assertEqual(self.longest_sleeper.id, '10')
        self.assertEqual(self.longest_sleeper.find_most_asleep_minute(), 24)
        self.assertEqual(self.list_of_guards['99'].find_most_asleep_minute(), 45)



    def test_list_of_days(self):
        self.assertEqual(len(self.list_of_days), 5)
        self.assertEqual(list(self.list_of_days.values())[0].id, '10')
        self.assertEqual(list(self.list_of_days.values())[1].id, '99')
        self.assertEqual(list(self.list_of_days.values())[2].id, '10')
        self.assertEqual(list(self.list_of_days.values())[3].id, '99')
        self.assertEqual(list(self.list_of_days.values())[4].id, '99')
        
    def test_log_entry_time(self):
        self.assertEqual(self.entries[0].time.tm_year, 1518)
        self.assertEqual(self.entries[0].time.tm_mon, 11)
        self.assertEqual(self.entries[0].time.tm_mday, 1)
        self.assertEqual(self.entries[0].time.tm_hour, 0)
        self.assertEqual(self.entries[0].time.tm_min, 0)

    def test_log_entry_type(self):
        self.assertEqual(self.entries[0].id, '10')
        self.assertEqual(self.entries[0].type, 'id')
        self.assertEqual(self.entries[1].type, 'down')
        self.assertEqual(self.entries[2].type, 'up')

    def tearDown(self):
        del self.entries

class Test_TestDays(unittest.TestCase):

    def test_day3_special_area(self):
        test_area_list = day3.Area_List(['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2'])
        self.assertEqual(test_area_list.find_unoverlapping_area(), 3)

    def test_day3_test_area_overlap(self):
        test_area_list = day3.Area_List(['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2'])
        self.assertEqual(test_area_list.area_list[0].has_overlap(test_area_list.area_list[0]), True)
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