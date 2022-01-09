class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        unique_list = []
        for x in nums:
            if x not in unique_list:
                unique_list.append(x)
        if len(unique_list)>=3:
            return unique_list[-3]
        else:
            return unique_list[-1]