class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        in_bound = lambda row, col: 0 <= row < n and 0 <= col <m
        visited_coord = set()
        DIR = [[0,1],[1,0],[-1,0],[0,-1]]
        arr = [0]
        
        def dfs(row, col, grid, arr, area):
            visited_coord.add((row, col))
            area[0] += 1
            for d in DIR:
                new_row, new_col = row + d[0], col + d[1]
                if (new_row, new_col) in visited_coord or not in_bound(new_row, new_col) or grid[new_row][new_col] == 0:
                    continue
                dfs(new_row, new_col, grid, arr, area)  
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    if (i, j) not in visited_coord:
                        area = [0]
                        dfs(i, j, grid, arr,area)
                        arr[0] = max(area[0], arr[0])
        return arr[0]