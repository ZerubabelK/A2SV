class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(row, col, count):
            if 0 <= row < n and 0 <= col < m and grid[row][col] != -1:
                if grid[row][col] == 2: 
                    if count == steps:
                        result[0] += 1
                    return
                
                grid[row][col] = -1
                for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
                    new_row, new_col = row+i, col+j
                    dfs(new_row, new_col, count+1)
                grid[row][col] = 0
        
        if not grid: return 0
        n = len(grid)
        m = len(grid[0])
        steps = 0
        
        for row in range(n): 
            for col in range(m):
                if grid[row][col] == 1:
                    start_r, start_c = row, col
                elif grid[row][col] == 0:
                    steps += 1   
        result = [0]
        dfs(start_r, start_c, -1)             
        
        return result[0]
