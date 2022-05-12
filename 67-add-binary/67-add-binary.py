class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = list(a), list(b)
        for i in range(len(a)):
            a[-(i+1)] = 2 ** i * int(a[-(i+1)])
        for i in range(len(b)):
            b[-(i+1)] = 2 ** i * int(b[-(i+1)])
        return str(bin(sum(a) + sum(b)))[2:]