class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l <= r:
            mid = l + (r-l)//2
            time = self.helper(piles, mid)
            if time > h:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def helper(self, piles, k):
        time = 0
        for pile in piles:
            time += math.ceil(pile/k)
        return time