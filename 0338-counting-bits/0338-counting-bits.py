class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        for i in range(n+1):
            bits = bin(i)
            ans[i] += sum([int(x) for x in bits[2:]])
        return ans