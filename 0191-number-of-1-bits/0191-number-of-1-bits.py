class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = bin(n)
        ans = 0
        for bit in bits:
            if bit == '1':
                ans += 1
        return ans