class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        def dp(count, memo = {}):
            if count > high:
                return 0
            if count in memo:
                return memo[count]
            
            res = dp(count + zero, memo) + dp(count + one, memo)
            
            memo[count] = res + 1  if count >= low else res
            
            return memo[count] % (10**9 + 7)
        
        return dp(0) 
        
            