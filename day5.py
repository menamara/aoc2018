from aoc_helpers import dataio

def reduce(string_input):
    """ Reduce the input from all adjacent characters that are the same letter and differend case."""
    str = list(string_input)
    lentgh = len(string_input)
    i = 0
    while i < lentgh-1:
        if (abs(ord(str[i])-ord(str[i+1])) == 32):
            str[i:i+2] = []
            lentgh -= 2
            i -= 1
        else:
            i += 1
        
    return ''.join(str)


class Polymer:
    def __init__(self, input_string):
        self.string = input_string

    def reduced_length(self):
        return len(reduce(self.string))

if __name__ == '__main__':
    data = dataio.load_data(5)
    input = dataio.split_data(data,'\n')
    polymer = Polymer(input[0])

    print(' '.join(['The solution for day 4 part 1 = ', 
                    str(polymer.reduced_length())]))
    print(' '.join(['The solution for day 4 part 2 =',
                    '']))