class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        for i, num in enumerate(nums):
            for j in range(i+1, len(nums)):
                b = nums[j] - num
                if (i,b) not in dp: 
                    dp[j,b] = 2
                else:
                    dp[j,b] = dp[i,b] + 1
        return max(dp.values())