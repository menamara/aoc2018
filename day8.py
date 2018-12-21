from aoc_helpers import dataio

class Licence:
    def __init__(self, data):
        self.data = data
        self.idx = 0
        self.md_sum = 0        

    def process_node(self):
        n_mdata = self.data[self.idx+1]
        if self.data[self.idx] == 0:
            self.md_sum += sum(self.data[self.idx+2:self.idx+2+n_mdata])
            del self.data[self.idx:self.idx+2+n_mdata]
            self.idx -= 2
            if self.idx < 0: 
                print(str(self.md_sum))
                return self.md_sum
            self.data[self.idx] -= 1
        else:
            self.idx += 2
        return self.process_node()
        

if __name__ == '__main__':
    data = dataio.load_data(8)
    input = int(dataio.split_data(data,'\n'))
    licence = Licence(input)
    

    print(' '.join(['The solution for day 8 part 1 =', 
                   str(licence.process_node())]))
    print(' '.join(['The solution for day 8 part 2 =',
                   '']))


