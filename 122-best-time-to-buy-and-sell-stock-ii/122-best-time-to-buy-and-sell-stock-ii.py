class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        res = 0
        for i in range(len(prices) - 1):
            dp[i] = prices[i+1] - prices[i]
            res = max(dp[i] + res, res)
        return res