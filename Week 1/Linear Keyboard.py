t = int(input())
for i in range(t):
    tot_time = 0
    test_case = input()
    case = input()
    for j in range(1, len(case)):
        prev_pos = test_case.index(case[j - 1]) + 1
        curr_pos = test_case.index(case[j]) + 1
        time = abs(prev_pos - curr_pos)
        tot_time += time
    print(tot_time)