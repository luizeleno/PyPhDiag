def markers():
    '''
        Function to generate markers sequentially
    '''
    mkr_list = ['o', 's', 'v', '^', '<', '>', 'P', '*', 'D']
    N = len(mkr_list)
    n = 0
    while n < N:
        yield mkr_list[n] + '-'
        n += 1
    else:
        n = 0
        yield mkr_list[n] + '-'
