from aoc_helpers import dataio
from collections import Counter

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


if __name__ == '__main__':
    data = dataio.load_data(2)
    input = dataio.split_data(data)
    print(' '.join(['The solution for day 2 part 1 =', str(checksum(input))]))
    print(' '.join(['The solution for day 2 part 2 =', "??"]))