import re
import time as t
import itertools
from aoc_helpers import dataio

class Log_Entry:
    """ A log entry with a date and a type.
    
    Type can be 
    'up'   -- if the guard woke up at this time
    'down' -- if the guard fell asleep at this time
    'id'   -- if the guard came on duty, in this case the id is also saved
    """
        
    def __init__(self, line_string):
        """ Initiate the log entry and format its attributes.
        
        Examples
        [1518-11-01 00:00] Guard #10 begins shift
        [1518-11-01 00:05] falls asleep
        [1518-11-01 00:25] wakes up
         """

        attributes = re.match(
            r"\[(?P<time>[\d\-\: ]*)\] (?P<entry>.*)", line_string)
        self.time = t.strptime(attributes.group('time'), "%Y-%m-%d %H:%M")
        self.yday= self.time.tm_yday

        if attributes.group('entry') == 'falls asleep':
            self.type = 'down'
        elif attributes.group('entry') == 'wakes up':
            self.type = 'up'
        else:
            self.type = 'id'
            self.id = re.match(r'.*#(?P<id>\d+).*', attributes.group('entry')).group('id')
            if  self.time.tm_hour == 23:
                self.yday += 1


class Day:
    """ A day holds a date, the id of the guard and up and down times.
    
    The day of the year (yday) functions as id for each day.
    """

    def __init__(self, log_entry):
        self.date = log_entry.yday
        self.down = []
        self.up= []
        self.id = []
        self.add_to_log(log_entry)

    def add_to_log(self, log_entry):
        assert(self.date == log_entry.yday)
        if log_entry.type == 'down':
            self.down.append(log_entry.time.tm_min) 
        elif log_entry.type == 'up':
            self.up.append(log_entry.time.tm_min) 
        else:
            self.id = log_entry.id

    def count_asleep_minutes(self):
        minutes_asleep = 0
        assert(len(self.up)==len(self.down))
        for fall_asleep_minute, wake_up_minute in zip(sorted(self.down), sorted(self.up)):
            minutes_asleep += (wake_up_minute - fall_asleep_minute)
        return minutes_asleep

    def get_asleep_minutes(self):
        asleep_minutes = [] 
        for fall_asleep_minute, wake_up_minute in zip(sorted(self.down), sorted(self.up)):
            asleep_minutes.extend(list(range(fall_asleep_minute, wake_up_minute)))
        return asleep_minutes

class Guard:
    """ A guard has an id and a list of days when he was on duty."""
    def __init__(self, day):
        self.id = day.id
        self.days = [day]
    
    def add_day(self, day):
        assert(day.id == self.id)
        self.days.append(day)

    def count_asleep_minutes(self):
        minutes_asleep = 0
        for day in self.days:
            minutes_asleep += day.count_asleep_minutes()
        return minutes_asleep
    
    def count_most_asleep_minute(self):
        minutes = bytearray(60)
        for day in self.days:
            asleep_minutes = day.get_asleep_minutes()
            for minute in asleep_minutes:
                minutes[minute] += 1
        most_asleep_minute = minutes.index(max(minutes))
        return (most_asleep_minute, max(minutes))

    def find_most_asleep_minute(self):
        return self.count_most_asleep_minute()[0]

def compile_list_of_days(input):
    list_of_days = {}
    for line in input:
        entry = Log_Entry(line)
        yday = entry.yday 
        if yday in list_of_days:
            list_of_days[yday].add_to_log(entry)
        else:
            list_of_days[yday] = Day(entry)
    return list_of_days
    
def assign_days_to_guards(input):
    list_of_days = compile_list_of_days(input)
    list_of_guards = {}
    for day in list_of_days.values():
        if day.id in list_of_guards:
            list_of_guards[day.id].add_day(day)
        else:
            list_of_guards[day.id] = Guard(day)
    return list_of_guards

def find_longest_sleeper(input):
    list_of_guards = assign_days_to_guards(input)
    longest_sleeper = []
    max_sleep_time = 0
    for guard in list_of_guards.values():
        sleep_time = guard.count_asleep_minutes()
        if max_sleep_time < sleep_time:
            max_sleep_time = sleep_time 
            longest_sleeper = guard
    return longest_sleeper

def find_most_consistent_sleeper(input):
    list_of_guards = assign_days_to_guards(input)
    max_days = 0
    answer = 0
    sleep_record = []
    for guard in list_of_guards.values():
        sleep_record = guard.count_most_asleep_minute()
        if max_days < sleep_record[1]:
            max_days = sleep_record[1]
            answer = int(guard.id) * sleep_record[0]
    return answer


if __name__ == '__main__':
    data = dataio.load_data(4)
    input = dataio.split_data(data,'\n')
    longest_sleeper = find_longest_sleeper(input)
    answer1 = longest_sleeper.find_most_asleep_minute() * int(longest_sleeper.id)

    print(' '.join(['The solution for day 4 part 1 = ', 
                    str(answer1)]))
    print(' '.join(['The solution for day 4 part 2 =',
                    str(find_most_consistent_sleeper(input))]))