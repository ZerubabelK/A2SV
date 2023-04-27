class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        freshCount, minutes = 0, 0
        q = deque()
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    freshCount += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        
        def bfs():
            nonlocal minutes, n, m, freshCount
            while q:
                for i in range(len(q)):
                    x, y = q.popleft()
                    # print(x, y)
                    for dx, dy in directions:
                        newX, newY = x + dx, y + dy
                        
                        if newX not in range(n) or newY not in range(m) or grid[newX][newY] != 1:
                            continue
                        if newX in range(n) and newY in range(m):  
                            grid[newX][newY] = 2
                            q.append((newX, newY))
                            freshCount -= 1
                if q:
                    minutes += 1
                    
        bfs()    
        if freshCount:
            return -1
        return minutes
        