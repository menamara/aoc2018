from utils import dataio
import re

def add(input, init_value = 0):
    result = init_value
    for number in input:
        result += number
    return result


if __name__ == '__main__':
    data = dataio.load_data(1)
    lines = re.split('\n', data)
    lines = list(filter(None, lines))
    input = list(map(int, lines))
    print(add(input))