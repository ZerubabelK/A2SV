class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        ops = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                ops += 1
                for j in range(i+1, len(nums)):
                    nums[j] -= nums[i]
        return ops