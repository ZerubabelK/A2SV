class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
        for i in range(len(nums)):
            if prefix[i] == prefix[-1] - prefix[i+1]:
                return i
        return -1