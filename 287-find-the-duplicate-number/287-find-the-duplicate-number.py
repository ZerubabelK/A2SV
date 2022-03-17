class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = [0] * 100001
        
        for i in range(len(nums)):
            if arr[nums[i]] == 1:
                return nums[i]
            arr[nums[i]] = 1
        