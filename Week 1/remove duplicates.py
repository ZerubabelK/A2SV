class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set(nums)
        if len(s) == len(nums):
            return len(nums)
        else:
            for i,val in enumerate(s):
                nums[i] = val
            for i,val in enumerate(sorted(nums[:len(s)])):
                nums[i] = val
            return len(s)