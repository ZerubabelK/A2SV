class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(row, col):
            if not inbound(row, col):
                return 0
            if (row, col) in memo:
                return memo[(row, col)]
            if (row, col) == (m - 1, n - 1):
                return 1
            paths = dfs(row + 1, col) + dfs(row, col + 1)
            memo[(row, col)] = paths
            return paths
        inbound = lambda row, col: 0 <= row < m and 0 <= col < n
        
        return dfs(0, 0)