class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        for i in range(n):
            mx=nums[i]
            mn=nums[i]
            for j in range(i+1, n):
                if nums[j] > mx:
                    mx = nums[j]
                elif nums[j] < mn:
                    mn = nums[j]
                res += (mx-mn)
    
        return res