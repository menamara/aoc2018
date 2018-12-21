import re
import itertools
from aoc_helpers import dataio

def create_graph(input_data):
    graph = {}
    for line in input_data:
        node = re.match(
            r"Step (?P<parent>[A-Z]).*(?P<child>[A-Z]).*", line).groupdict()
        if not node['child'] in graph:#node exists
            graph[node['child']] = [node['parent']]
        else:
            graph[node['child']].append(node['parent'])
    return graph

def order(input_data):
    graph = create_graph(input_data)
    available = list(
        set().union(*graph.values()) - set(graph.keys()))
    result = ''
    while len(available) > 0:
        available.sort()
        next_item = available.pop(0)
        if next_item in graph:
            graph.pop(next_item)
        for key, values in graph.items():
            if next_item in values:
                values.remove(next_item) 
            if (not values) and (key not in available):
                available.append(key)
        result = ''.join([result,next_item])
    return result


def schedule(input_data, n_worker, t_overhead):
    worker = list(map(list, 
        zip(n_worker * [ '' ], n_worker * [ 0 ])))
    graph = create_graph(input_data)
    ready = list(
        set().union(*graph.values()) - set(graph.keys()))
    available = []
    t = 0
    while len(graph) > 0 or len(ready) > 0:
        # go through each worker
        available.extend(ready)
        available.sort()
        for a in ready :
            if a in graph:
                graph.pop(a)
        ready = []
        for w in worker:
            # assign available tasks if free
            if w[ 1 ] == 0 and len(available) > 0:
                a = available.pop(0)
                if a in graph:
                    graph.pop(a)
                w[ 0 ] = a
                w[ 1 ] = ord(a)-ord('A')+1 + t_overhead
            # receive ready tasks
            if w[ 1 ] == 1 and w [ 0 ] != '':
                for key, values in graph.items():
                # update graph
                    if w[ 0 ] in values:
                        values.remove(w[ 0 ]) 
                # update avaialbility list
                    if (not values) and (key not in available):
                        ready.append(key)
                w[ 0 ] = ''
            # increment time
            w [ 1 ] =  max(w[ 1 ]-1, 0)
        # increment global time
        t += 1
    t += max([w[ 1 ] for w in worker])
    return t
     
if __name__ == '__main__':
    data = dataio.load_data(7)
    input = dataio.split_data(data,'\n')

    print(' '.join(['The solution for day 7 part 1 =', 
                   order(input)]))
    print(' '.join(['The solution for day 7 part 2 =',
                   str(schedule(input,5,60))]))


