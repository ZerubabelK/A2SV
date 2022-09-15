class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dis = 0
        for bit in bin(x ^ y)[2:]:
            if bit == '1':
                dis += 1
        return dis