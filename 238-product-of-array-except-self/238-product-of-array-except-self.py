class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        for i in range(len(nums)-1):
            left.append(left[-1] * nums[i])
        for i in range(len(nums)-1, 0, -1):
            right.append(right[-1] * nums[i])
        right.reverse()
        
        return [left[i] * right[i] for i in range(len(nums))]