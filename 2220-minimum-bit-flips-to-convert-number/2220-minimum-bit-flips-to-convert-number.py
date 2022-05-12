class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        cnt = 0
        res = bin(start ^ goal)
        for i in res:
            if i == '1':
                cnt += 1
        return cnt