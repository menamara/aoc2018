from aoc_helpers import dataio

class Area:
    """ An object with an ID, a top left corner, a width and height. """
        
    def __init__(self, line_string):
        """ Initiate the Area with all attributes. """
        self.area = []

    def size(self):
        """ Calculate the size of an area. """
        return 0

    def overlap(self, other):
        """ return the overlap between two areas, empty if they do not overlapp """
        return []



class Area_List:
    """ A list of Areas. """
    def __init__(self, input):
        self.area_list =[]
        for line in input:
            self.area_list.append(Area(line))
    
    def list_overlapps(self):
        """ Compile a list of the overlap between each overlapping pair of areas. """
        self.overlap = []
    
    def count_overlap_area(self):
        """ Calculate the size of the overlap of all areas in the list. """
        # ToDo
        # call list_overlap if self.overlap is still empty
        # use reduce and count for each pair of areas in self.overlap the 
        # area unique to the first area
        # 1. calculate size of first area and substract size of overlap area
        return 0



if __name__ == '__main__':
    data = dataio.load_data(3)
    input = dataio.split_data(data)
    print(' '.join(['The solution for day 3 part 1 =', '']))
    print(' '.join(['The solution for day 3 part 2 =', '']))