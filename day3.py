import re
import numpy
from aoc_helpers import dataio

class Area:
    """ An object with an ID, a top left corner, a width and height. """
        
    def __init__(self, line_string):
        """ Initiate the Area with all attributes. """
        attributes = re.match(
            r"#(?P<id>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<dx>\d+)x(?P<dy>\d+)",
            line_string)
        self.id = int(attributes.group('id'))
        self.x = int(attributes.group('x'))
        self.y = int(attributes.group('y'))
        self.dx = int(attributes.group('dx'))
        self.dy = int(attributes.group('dy'))
        self.area = self.dx * self.dy

    def overlap(self, other):
        """ return the overlap between two areas, empty if they do not overlapp """
        return []



class Area_List:
    """ A list of Areas. """
    def __init__(self, input):
        self.area_list =[]
        for line in input:
            self.area_list.append(Area(line))
    
    def count_overlap_linear(self, total_size = 1000):
        """ Calculate the size of the overlap of all areas in the list. """
        canvas = numpy.zeros((total_size,total_size))
        for area in self.area_list:
            canvas[area.y:(area.y+area.dy), area.x:(area.x+area.dx)] += 1
        return  numpy.sum(canvas > 1)



if __name__ == '__main__':
    data = dataio.load_data(3)
    input = dataio.split_data(data,'\n')
    areas = Area_List(input)
    print(' '.join(['The solution for day 3 part 1 = ', 
                    str(areas.count_overlap_linear()) ]))
    print(' '.join(['The solution for day 3 part 2 =', '']))