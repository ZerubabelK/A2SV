class Solution:
    def jump(self, nums: List[int]) -> int:
        def dp(i, memo = {}):
            if i == len(nums)-1:
                return 0
            if i >= len(nums):
                return float('inf')
            if i in memo:
                return memo[i]
            temp = float('inf')
            for j in range(i+1, i + nums[i] + 1):
                temp = min(temp, dp(j, memo))
            memo[i] = temp + 1
            return memo[i]
        return dp(0)