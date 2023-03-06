class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = defaultdict(int)
        running_sum = 0
        count = 0
        for num in nums:
            prefix[running_sum] += 1
            running_sum += num
            if running_sum - goal in prefix:
                count += prefix[running_sum - goal]
        return count