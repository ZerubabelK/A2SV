class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            gcd = nums[i]
            count += 1 if gcd == k else 0
            for j in range(i+1, len(nums)):
                gcd = self.findGCD(nums[j], gcd)
                if gcd == k:
                    count += 1
                elif gcd < k:
                    break
        return count
            
    def findGCD(self, x, y):
        if y == 0:
            return x
        return self.findGCD(y, x % y)