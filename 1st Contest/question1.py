def equilateral(n):
    for i in range(n):
        print(" "*(n-(i+1)),end='')
        print('*'*(2*(i+1)-1))
equilateral(6)

def right_angled(n):
    for i in range(n):
        print('*'*(i+1))
        
right_angled(5)
