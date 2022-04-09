class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        purchase, sold, profit = [float('inf'), -1], [float('-inf'), -1], 0
        
        for i in range(len(prices)):
        
            if prices[i] < purchase[0]:
                purchase = [prices[i], i]
            if purchase[1] > sold[1]:
                sold = purchase
            if prices[i] > sold[0]:
                sold = [prices[i], i]
                
            profit = max(profit, sold[0] - purchase[0])
            
        return profit