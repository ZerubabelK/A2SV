class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == nums[mid - 1] or nums[mid] == nums[mid + 1]:
                return nums[mid]
            elif nums[mid] > mid:
                left = mid + 1
            else:
                right = mid - 1
        