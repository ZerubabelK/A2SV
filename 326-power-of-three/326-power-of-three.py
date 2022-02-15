class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if int(n) == 0:
            return False
        if n == 1:
            return True
        return True and self.isPowerOfThree(n/3) 