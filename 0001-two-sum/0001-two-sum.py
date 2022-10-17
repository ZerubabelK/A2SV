class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        indices = [-1,-1]
        for i in range(len(nums)):
            other_number = target - nums[i]
            if other_number in seen:
                first_index = i
                second_index = seen[other_number]
                indices = [first_index, second_index]
            else:
                seen[nums[i]] = i
        return indices