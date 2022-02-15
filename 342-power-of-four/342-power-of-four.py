class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if int(n) == 0:
            return False
        if n == 1:
            return True
        return True and self.isPowerOfFour(n/4)