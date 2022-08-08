class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {}
        def dp(i, flag = False):
            _max = -float('inf')
            if i == len(nums)-1:
                return nums[i]
            if i in memo:
                return memo[i]
            if flag:
                return nums[i]
            else:
                _max = max(dp(i + 1, True), dp(i + 1, False))
            _max = max(_max + nums[i], nums[i])
            memo[i] = _max
            return _max
        
        res = -float('inf')
        for i in range(len(nums)):
            res = max(res, dp(i))
        return res