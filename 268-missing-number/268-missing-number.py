class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for num in nums:
            ans ^= n ^ num
            n -= 1
        return ans