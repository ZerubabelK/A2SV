class Solution:
    def jump(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            if i == len(nums)-1:
                return 0
            if i >= len(nums):
                return float('inf')
            temp = float('inf')
            for j in range(i+1, i + nums[i] + 1):
                temp = min(temp, dp(j))
            return temp + 1
        return dp(0)