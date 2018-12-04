import re
import time as t
import numpy
import itertools
from aoc_helpers import dataio

class Log_Entry:
    """ A log entry with id, Date and time and fall asleep or wakeup information."""
        
    def __init__(self, line_string):
        """ Initiate the log entry and format its attributes.
        
        Examples
        [1518-11-01 00:00] Guard #10 begins shift
        [1518-11-01 00:05] falls asleep
        [1518-11-01 00:25] wakes up
         """

        self.id = '0'

        attributes = re.match(
            r"\[(?P<time>[\d\-\: ]*)\] (?P<entry>.*)", line_string)
        self.time = t.strptime(attributes.group('time'), "%Y-%m-%d %H:%M")

        if attributes.group('entry') == 'falls asleep':
            self.type = 'down'
        elif attributes.group('entry') == 'wakes up':
            self.type = 'up'
        else:
            self.type = 'id'
            self.id = re.match(r'.*#(?P<id>\d+).*', attributes.group('entry')).group('id')

if __name__ == '__main__':
    data = dataio.load_data(3)
    input = dataio.split_data(data,'\n')
    print(' '.join(['The solution for day 4 part 1 = ', 
                    '']))
    print(' '.join(['The solution for day 4 part 2 =',
                    '']))