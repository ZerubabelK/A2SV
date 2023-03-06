class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        _max = 0
        for i in range(len(arr)):
            if arr[i] > arr[_max]:
                _max = i
        return _max