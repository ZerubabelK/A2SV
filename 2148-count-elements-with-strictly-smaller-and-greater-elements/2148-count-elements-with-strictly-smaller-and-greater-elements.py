class Solution:
    def countElements(self, nums: List[int]) -> int:
        _min = float('inf')
        _max = -float('inf')
        for num in nums:
            _max = max(num, _max)
            _min = min(num, _min)
        cnt = 0
        for num in nums:
            if num < _max and num > _min:
                cnt += 1
        print(_max, _min)
        return cnt