class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        arr = [0] * 1001
        for b, d in logs:
            for i in range(b, d):
                arr[i - 1950] += 1
        _max = 0
        for i in range(len(arr)):
            if arr[i] > arr[_max]:
                _max = i
        return 1950 + _max