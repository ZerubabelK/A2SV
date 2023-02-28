class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        _max = max(Counter(nums).values())
        _dict = defaultdict(list)
        ans = len(nums)
        for i in range(len(nums)):
            if len(_dict[nums[i]]) + 1 == _max:
                ans = min(ans, i - (_dict[nums[i]][0] if len(_dict[nums[i]]) > 0 else 0) + 1)
            else:
                _dict[nums[i]].append(i)
        return ans