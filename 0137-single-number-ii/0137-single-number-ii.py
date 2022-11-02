class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pbits = [0] * 32
        nbits = [0] * 32
        for num in nums:
            index = -1
            if num < 0:
                num *= -1
                while num != 0:
                    bit = num & 1
                    nbits[index] += bit
                    index -= 1
                    num = num >> 1
            else:
                while num != 0:
                    bit = num & 1
                    pbits[index] += bit
                    index -= 1
                    num = num >> 1
        single = 0
        neg = False
        for i in range(32):
            if (nbits[-(i + 1)] % 3 != 0):
                single += 1 << i
                neg = True
            elif (pbits[-(i + 1)] % 3 != 0):
                single += 1 << i
        return (-single) if neg else single