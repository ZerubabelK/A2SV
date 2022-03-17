class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        def trips(times):
            t = 0
            for i in range(len(time)):
                t += times // time[i]
                
            return t
        res = 0
        left = 1
        right = max(time) * totalTrips
        while left <= right:
            mid = (left + right) // 2
            
            if trips(mid) < totalTrips:
                left = mid + 1
            else:
                res = mid
                right = mid - 1
                
        return res