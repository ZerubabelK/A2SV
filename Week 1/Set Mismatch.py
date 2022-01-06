class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        missing = [i for i in range(1,len(nums)+1) if i not in nums]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                missing.append(nums[i])
        return [missing[1],missing[0]]