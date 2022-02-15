class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = len(nums)-1
        while k > 0:
            temp = nums.pop()
            nums.insert(0, temp)
            k -= 1