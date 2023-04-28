class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        n, m = len(mat), len(mat[0])
        inbound = lambda r, c: 0 <= r < n and 0 <= c < m
        queue = deque()
        visited = set()
        for i in range(n):
            for j in range(m):
                if not mat[i][j]:
                    queue.append((i, j))
                    visited.add((i, j))
        answer = [[0 for _ in range(m)] for _ in range(n)]
        level = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                r, c = queue.popleft()
                answer[r][c] = level if mat[r][c] else answer[r][c]
                for x, y in direction:
                    nr, nc = r + x, c + y
                    if inbound(nr, nc) and mat[nr][nc] and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            level += 1
                        
        return answer