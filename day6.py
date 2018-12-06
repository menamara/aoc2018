import numpy
from collections import Counter
from aoc_helpers import dataio

class Association_Map:
    def __init__(self, input_string):
        self.anchor = []
        for line in input_string:
            self.anchor.append(
                list(map(int, dataio.split_data(line))))
        self.xmax = max(xy[0] for xy in self.anchor) + 1
        self.ymax = max(xy[1] for xy in self.anchor) + 1
        self.xmin = min(xy[0] for xy in self.anchor) - 1
        self.ymin = min(xy[1] for xy in self.anchor) - 1

    def max_area(self):
        xmax = self.xmax
        ymax = self.ymax
        xmin = self.xmin
        ymin = self.ymin
        equal_dist_flag = len(self.anchor) + 10
        aso_map = numpy.zeros((xmax-xmin, ymax-xmin))
        for x in range(xmin, xmax):
            for y in range(ymin, ymax):
                dist_list = []
                for coord in self.anchor:
                    dist_list.append(manhattan_dist ([x,y], coord))
                if Counter(dist_list)[min(dist_list)] > 1:
                    aso_map[x-xmin, y-ymin] = equal_dist_flag
                else:
                    aso_map[x-xmin, y-ymin] = dist_list.index(min(dist_list))
        area_flags, cnt = numpy.unique(aso_map, return_counts=True)
        area_counts = dict(zip(area_flags, cnt))
        borders = numpy.unique(numpy.concatenate(
            [aso_map[:,0], aso_map[0], aso_map[-1],aso_map[:,-1]]))
        for value in borders:
            del area_counts[value] 
        return max(area_counts.values())


def manhattan_dist(x, y):
    return abs(y[0] - x[0]) + abs(y[1] - x[1])

if __name__ == '__main__':
    data = dataio.load_data(6)
    input = dataio.split_data(data,'\n')
    asso_map = Association_Map(input)

    print(' '.join(['The solution for day 6 part 1 =', 
                   str(asso_map.max_area())]))
    print(' '.join(['The solution for day 6 part 2 =',
                    '']))