from aoc_helpers import dataio

class Association_Map:
    def __init__(self, input_string):
        self.anchor = []
        self.xmax = 0
        self.ymax = 0 
        self.xmin = 0
        self.ymin = 0

    def max_area(self):
        return 0


if __name__ == '__main__':
    data = dataio.load_data(6)
    input = dataio.split_data(data,'\n')
    asso_map = Association_Map(input)

    print(' '.join(['The solution for day 4 part 1 =', 
                    '']))
    print(' '.join(['The solution for day 4 part 2 =',
                    '']))