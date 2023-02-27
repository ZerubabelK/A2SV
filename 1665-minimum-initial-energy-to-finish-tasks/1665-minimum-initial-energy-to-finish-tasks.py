class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: x[0] - x[1])
        ans = 0
        c_min = 0
        for cost, _min in tasks:
            if _min > c_min:
                ans += (_min - c_min)
                c_min = _min
            c_min -= cost
        return ans