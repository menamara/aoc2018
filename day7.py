import re
from aoc_helpers import dataio

def create_graph(input_data):
    graph = {}
    for line in input_data:
        node = re.match(
            r"Step (?P<parent>[A-Z]).*(?P<child>[A-Z]).*", line).groupdict()
        if not node('child') in graph:#node exists
            graph[node('child')] = [node('parent')]
        else:
            graph[node('child')].append(node('parent'))
    return graph

if __name__ == '__main__':
    data = dataio.load_data(7)
    input = dataio.split_data(data,'\n')


    print(' '.join(['The solution for day 7 part 1 =', 
                   '']))
    print(' '.join(['The solution for day 7 part 2 =',
                   '']))


