class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        ans = 0
        left = 1
        right = 10**6
        
        while left <= right:
            mid = (left + right) // 2
            tot = 0
            
            for num in nums:
                tot += math.ceil(num / mid)
                
            if tot > threshold:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1
                
        return ans
                
                