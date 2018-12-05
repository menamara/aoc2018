import string
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

def delete_char(string_input, del_char):
    str = list(string_input)
    lentgh = len(string_input)
    i = 0
    while i < lentgh:
        if str[i] == del_char or str[i]== del_char.swapcase():
            str[i:i+1] = []
            lentgh -= 1
            i -= 1
        else:
            i += 1
    return ''.join(str)

def find_shortest(polymer):
    min_len = polymer.reduced_length()
    for char in list(string.ascii_lowercase[:26]):
        next_len = polymer.reduced_length_with_broken_unit(char)
        if min_len > next_len:
            min_len = next_len
    return min_len    





class Polymer:
    def __init__(self, input_string):
        self.string = input_string
        self.broken_string = input_string

    def reduced_length(self):
        return len(reduce(self.string))

    def reduced_length_with_broken_unit(self, char):
        self.broken_string = delete_char(self.string, char)
        return len(reduce(self.broken_string))
        
    

if __name__ == '__main__':
    data = dataio.load_data(5)
    input = dataio.split_data(data,'\n')
    polymer = Polymer(input[0])

    print(' '.join(['The solution for day 4 part 1 =', 
                    str(polymer.reduced_length())]))
    print(' '.join(['The solution for day 4 part 2 =',
                    str(find_shortest(polymer))]))