class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.find(nums[:len(nums)-1]), self.find(nums[1:]))
    
    def find(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0
        for num in nums:
            dp = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = dp  
        return prev1