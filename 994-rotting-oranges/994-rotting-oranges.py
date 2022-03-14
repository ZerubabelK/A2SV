class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        minutes = 0
        DIR = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()
        in_bound = lambda row, col: 0<= row < n and 0 <= col < m
        queue = collections.deque()
        
        def bfs(minute = 0):                
            while queue:
                length = len(queue)
                
                for i in range(length):
                    node = queue.popleft()
                    for direction in DIR:
                        row, col = node[0] + direction[0], node[1] + direction[1]
                        
                        if (row, col) in visited or not in_bound(row, col) or grid[row][col] != 1:
                            continue
                
                        visited.add((row, col))   
                        grid[row][col] = 2
                        cnt[0] -= 1
                        queue.append((row, col))
                if queue:
                    minute += 1
            return minute
        cnt = [0]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i, j))
                if grid[i][j] == 1:
                    cnt[0] += 1
        minutes = bfs()          
        if cnt[0] > 0:
            return -1
        return minutes
