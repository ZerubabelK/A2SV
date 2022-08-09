class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        unique = set()
        nums.sort()
        for i in range(len(nums)):
            target = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if target > nums[left] + nums[right]:
                    left += 1
                elif target < nums[left] + nums[right]:
                    right -= 1
                else:
                    triplet = [nums[i], nums[left], nums[right]]
                    if tuple(triplet) in unique:
                        right -= 1
                        continue
                    res.append(triplet)
                    unique.add(tuple(triplet))
                    right -= 1
        return res