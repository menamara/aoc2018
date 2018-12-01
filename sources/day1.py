from utils import dataio
import re

def add(input, init_value = 0):
    result = init_value
    for number in input:
        result += number
    return result

def find_loop(input):
    buffer = bytearray(1000000)
    v = memoryview(buffer)
    result = 0
    while True:
        for number in input:
            if v[result] == 1:
                return result
            else:
                v[result] = 1
                result += number

if __name__ == '__main__':
    data = dataio.load_data(1)
    lines = re.split('\n', data)
    lines = list(filter(None, lines))
    input = list(map(int, lines))
    print(add(input))
    print(find_loop(input))