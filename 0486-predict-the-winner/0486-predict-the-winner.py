class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def getScore(l, r):
            if l == r:
                return nums[l]
            return max(nums[l] - getScore(l+1, r), nums[r] - getScore(l, r-1))
        
        return getScore(0,len(nums)-1) >= 0