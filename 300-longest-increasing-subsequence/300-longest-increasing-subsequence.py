class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        _max = 1
        memo = {}
        
        def dp(i):
            depth = 0

            if i in memo:
                return memo[i]
            
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    depth = max(dp(j), depth)
                    
            memo[i] = depth + 1
            return depth + 1
        
        for i in range(len(nums)):
            _max = max(dp(i), _max)
        return _max
            
            