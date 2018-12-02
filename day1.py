from aoc_helpers import dataio
import re

def add(input):
        return sum(input)

def find_loop(input, buffersize = 1000000 ):
    buffer = bytearray(buffersize)
    v = memoryview(buffer)
    min = 0
    max = 0
    result = 0
    while True:
        for number in input:
            if v[result] == 1:
                return result
            else:
                v[result] = 1
                result += number 
                # ensure we have no overflow
                if result < min:
                    min = result
                elif result > max:
                    max = result
                assert(max-min < buffersize)

if __name__ == '__main__':
    data = dataio.load_data(1)
    input = dataio.convert_to_int(data)
    print(' '.join(['The solution for day 1 part 1 =', str(add(input))]))
    print(' '.join(['The solution for day 1 part 2 =', str(find_loop(input))]))