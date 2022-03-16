class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0
        for i in range(len(grid)):
            index = -1
            left = 0
            right = len(grid[i]) - 1
            while left <= right:
                mid = (left + right) // 2
                if grid[i][mid] < 0:
                    right = mid - 1
                    index = mid
                else:
                    left = mid + 1
            if index >= 0:
                cnt += len(grid[i]) - index
        return cnt