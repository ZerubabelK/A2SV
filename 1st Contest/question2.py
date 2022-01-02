def weird_traingles(n):
    for i in range(n):
        print('*'*(i+1),end='')
        print(' '*2*(n-(i+1)),end='')
        print('*'*(i+1))

weird_traingles(4)
