class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        
        def dfs(i, buy):
            if i >= len(prices):
                return 0
            
            if (i, buy) in memo:
                return memo[(i, buy)]
            
            if buy:
                bought = dfs(i+1, False) - prices[i]
                cooldown = dfs(i+1, True)
                memo[(i, buy)] = max(bought, cooldown)
                
            else:
                sell = dfs(i+2, True) + prices[i]
                cooldown = dfs(i+1, False)
                memo[(i, buy)] = max(sell, cooldown)
            return memo[(i, buy)]
            
        return dfs(0, True)