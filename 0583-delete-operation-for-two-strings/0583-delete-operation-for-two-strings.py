class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length = self.bottomUp(word1, word2)
        return (len(word1) + len(word2)) - 2 * length
    
    def bottomUp(self, text1, text2):
        n, m = len(text1), len(text2)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1, n + 1):
                if text2[i-1] == text1[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
    
    def topDown(self, text1, text2, memo, i, j):
        if i >= len(text1) or j >= len(text2):
            return 0
        state = (i, j)
        if state in memo:
            return memo[state]
        if text1[i] == text2[j]:
            memo[state] = 1 + self.topDown(text1, text2, memo, i+1, j+1)
        else:
            memo[state] = max(self.topDown(text1, text2, memo, i, j+1), self.topDown(text1, text2, memo, i+1, j))
            
        return memo[state]