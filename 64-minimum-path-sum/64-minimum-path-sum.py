class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0] * len(grid[0]) for i in grid]
        DIR = [(-1,0), (0,-1)]
        inbound = lambda row, col: 0 <= row < len(grid) and 0 <= col <len(grid[0])
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i - 1 > -1 and j - 1 > -1:
                    grid[i][j] += min(grid[i-1][j], grid[i][j - 1])
                elif i - 1 > - 1:
                    grid[i][j] += grid[i - 1][j]
                elif j - 1 > - 1:
                    grid[i][j] += grid[i][j - 1]
                else:
                    continue
        return grid[len(grid)-1][len(grid[0])-1]