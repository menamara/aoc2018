import itertools
from collections import Counter
from aoc_helpers import dataio

def checksum(input):
    doubles = 0
    tripples = 0
    for line in input:
        c = Counter(line)
        v = c.values()
        if 2 in v:
            doubles += 1
        if 3 in v:
            tripples += 1
    return (doubles * tripples)

def is_match(string_a, string_b):
    diff = 0
    c = []
    for a, b in zip(string_a, string_b):
        if a == b:
            c.append(a)
        elif diff:
            # return empty string if more than 1 difference was encountered
            return ''
        else:
            diff = 1
    return ''.join(c)

def find_matching(input):
    for a, b in itertools.combinations(input, 2):
        c = is_match(a,b)
        if c != '' :
            return c
    return ''

if __name__ == '__main__':
    data = dataio.load_data(2)
    input = dataio.split_data(data)
    print(' '.join(['The solution for day 2 part 1 =', str(checksum(input))]))
    print(' '.join(['The solution for day 2 part 2 =', find_matching(input)]))