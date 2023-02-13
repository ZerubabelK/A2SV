class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque([(0,0)]) if not grid[0][0] else deque()
        DIR = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
        inbound = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid)
        visited = [[0 for _ in range(len(grid))] for _ in range(len(grid))]
        visited[0][0] = 1 if not grid[0][0] else 0
        path_length = 0
        while queue:
            path_length += 1
            length = len(queue)
            for _ in range(length):
                r, c = queue.popleft()
                for x, y in DIR:
                    nr, nc = r + x, c + y
                    if (r, c) == (len(grid) - 1, len(grid) - 1):
                        return path_length
                    if not inbound(nr, nc) or visited[nr][nc] or grid[nr][nc]:
                        continue
                    queue.append((nr, nc))
                    visited[nr][nc] = 1
        return -1