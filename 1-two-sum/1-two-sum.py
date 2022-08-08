class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _map = {}
        ans = []
        for i in range(len(nums)):
            if target - nums[i] in _map:
                ans = [i, _map[target - nums[i]]]
                break
            _map[nums[i]] = i
        return ans