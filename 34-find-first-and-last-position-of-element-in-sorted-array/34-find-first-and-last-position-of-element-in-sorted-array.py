class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        start, end = -1, -1
        
        while left <= right:
            mid = (left + right)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                start = mid
                right = mid - 1
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                end = mid
                left = mid + 1
        return [start, end]