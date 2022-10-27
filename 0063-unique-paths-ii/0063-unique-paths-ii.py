class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ## Top-down DP approach
        @cache
        def topDown(row, col, n, m):
            paths = 0
            if obstacleGrid[row][col]:
                return 0
            
            if (row, col) == (n-1, m-1):
                return 1
            
            for x, y in ((0,1),(1,0)):
                nr, nc = row + x, col + y
                if not in_bound(nr, nc):
                    continue
                paths += topDown(nr, nc, n, m)
            
            return paths
        
        ## Bottom-up DP approach
        def bottomUp(n, m):
            if obstacleGrid[0][0]:
                return 0
            dp = [[0 for _ in range(m)] for _ in range(n)]
            dp[n-1][m-1] = 1
            
            for r in range(n-1, -1, -1):
                for c in range(m-1,-1,-1):
                    for x, y in ((0,1),(1,0)):
                        nr, nc = r + x, c + y
                        if not in_bound(nr, nc) or obstacleGrid[nr][nc]:
                            continue
                        dp[r][c] += dp[nr][nc]
            return dp[0][0]
            
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        in_bound = lambda r, c: 0 <= r < n and 0 <= c < m
        return bottomUp(n, m)