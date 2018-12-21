test_data = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
idx = 0
md_sum = 0        

def process_node():
    global idx, test_data, md_sum
    n_mdata = test_data[idx+1]
    if test_data[idx] == 0:
        md_sum += sum(test_data[idx+2:idx+2+n_mdata])
        del test_data[idx:idx+2+n_mdata]
        idx -= 2
        if idx < 0: 
            print(str(md_sum))
            return
        test_data[idx] -= 1
    else:
        idx += 2
    process_node()
        

if __name__ == '__main__':
    #data = dataio.load_data(8)
    #input = int(dataio.split_data(data,'\n'))

    process_node()


    print(' '.join(['The solution for day 8 part 1 =', 
                   '']))
    print(' '.join(['The solution for day 8 part 2 =',
                   '']))


