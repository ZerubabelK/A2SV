def third_pattern(n):
    for i in range(2):
        for j in range(n):
            print('#'*(n-1),end=' ')
        print()

third_pattern(4)