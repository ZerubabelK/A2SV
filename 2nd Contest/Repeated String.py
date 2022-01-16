def repeatedString(s, n):
    # Write your code here
    m = n // len(s)
    r = n - (m*len(s))
    newS = s[:r]
    return list(newS).count('a') + s.count('a')*m