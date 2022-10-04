class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        coins = 0
        r = n-2
        for i in range(n//3):
            coins += piles[r]
            r-=2
        return coins
        