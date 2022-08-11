class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
        
        # def dp(i, tot = 0):
        #     depth = float('inf')
        #     if tot == amount:
        #         return 0
        #     for j in range(i, len(coins)):
        #         if tot + coins[j] > amount:
        #             continue
        #         depth = min(depth, dp(j, tot + coins[j]))
        #     return depth + 1
        # _min = float('inf')
        # for i in range(len(coins)):
        #     _min = min(_min, dp(i))   
        # if _min == float('inf'):
        #     return -1
        # return _min