class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str,nums))
        for i in range(len(nums)):
            maxim = i
            for j in range(i+1, len(nums)):
                if int(nums[j] + nums[maxim]) > int(nums[maxim] + nums[j]):
                    maxim = j
            tmp = nums[i]
            nums[i] = nums[maxim]
            nums[maxim] = tmp
        if len(set(nums)) == 1 and "0" in set(nums):
            return "0"
        return ''.join(nums)