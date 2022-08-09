class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for key in freq:
            if freq[key] > len(nums) / 2:
                return key