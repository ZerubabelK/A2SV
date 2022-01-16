def divisibleSumPairs(n, k, ar):
    # Write your code here
    tmp = [(ar[i],ar[j]) for i in range(len(ar)) for j in range(len(ar)) if i<j and (ar[i] + ar[j]) % k == 0]
    return len(tmp)