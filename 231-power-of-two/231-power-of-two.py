class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        cnt = 0
        while n > 0:
            if n % 2 == 1:
                cnt += 1
            n //= 2
        return cnt == 1