class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        t = []
        for i in range(0,len(nums)-1,2):
            t.append((nums[i],nums[i+1]))
        sum=0
        for p in t:
            sum+=min(p[0],p[1])
        return sum