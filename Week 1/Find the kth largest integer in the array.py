class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        nums.sort(key = lambda el: int(el))
        unique  = []
        for num in nums:
            if num not in unique:
                unique.append(num)
        return nums[-(k)]