class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
    
        def dfs(row, col):
            border = 0
            visited.add((row, col))
            for d in direction:
                nr, nc = row + d[0], col + d[1]
                if not inbound(nr, nc) or grid[nr][nc] == 0:
                    border += 1
                    continue
                if (nr, nc) in visited:
                    continue
                border += dfs(nr, nc)
            return border
        visited = set()
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        inbound = lambda r, c: 0 <= r < n and 0 <= c < m
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return dfs(i,j)
        
                    