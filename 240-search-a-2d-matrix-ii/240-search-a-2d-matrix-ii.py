class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def dfs(row, col):
            nonlocal _ans
            _ans = matrix[row][col] == target or _ans
            visited.add((row, col))
            for d in DIR:
                n_row, n_col = row + d[0], col + d[1]
                if (n_row, n_col) in visited or not inbound(n_row, n_col):
                    continue
                dfs(n_row, n_col)
        
        m, n = len(matrix), len(matrix[0])
        DIR = [(0,1),(1,0),(-1,0),(0,-1)]
        inbound = lambda row, col: 0 <= row < m and 0 <= col < n
        visited = set()
        _ans = False
        dfs(0, 0)
        return _ans