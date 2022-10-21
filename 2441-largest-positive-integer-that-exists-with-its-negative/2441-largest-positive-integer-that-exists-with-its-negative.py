class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        ans = -1
        for num in nums:
            if num * -1 in seen:
                ans = max(abs(num), ans)
            seen.add(num)
        return ans