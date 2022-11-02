class Solution:
    def findComplement(self, num: int) -> int:
        power = 0
        complement = 0
        while num != 0:
            bit = num & 1
            complement += (2 ** power) * (1 if bit == 0 else 0)
            power += 1
            num = num >> 1
        return complement