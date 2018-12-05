from aoc_helpers import dataio

def reduce(string_input):
    """ Reduce the input from all adjacent characters that are the same letter and differend case."""
    return ''

class Polymer:
    def __init__(self, input_string):
        self.string = input_string

    def reduced_length(self):
        return len(reduce(self.string))

if __name__ == '__main__':
    data = dataio.load_data(5)
    input = dataio.split_data(data,'\n')

    print(' '.join(['The solution for day 4 part 1 = ', 
                    '']))
    print(' '.join(['The solution for day 4 part 2 =',
                    '']))