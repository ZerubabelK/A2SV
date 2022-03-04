class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [i * -1 for i in nums]
        heapify(nums)
        for i in range(k - 1):
            heappop(nums)
        return nums[0] * -1