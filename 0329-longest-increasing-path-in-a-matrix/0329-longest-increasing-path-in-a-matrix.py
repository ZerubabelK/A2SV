class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        adj = defaultdict(list)
        indegree = defaultdict(int)
        DIR = ((0,1),(1,0),(-1,0),(0,-1))
        n, m = len(matrix),len(matrix[0])
        inbound = lambda x, y: 0 <= x < n and 0 <= y < m
        for i in range(n):
            for j in range(m):
                if (i, j) not in indegree:
                    indegree[(i,j)] = 0
                for x, y in DIR:
                    nx, ny = i + x, j + y
                    if not inbound(nx, ny):
                        continue
                    if matrix[i][j] < matrix[nx][ny]:
                        adj[(i, j)].append((nx, ny))
                        indegree[(nx, ny)] += 1
        que = deque()
        for key in indegree:
            if indegree[key] == 0:
                que.append(key)
        ans = 0
        while que:
            ans += 1
            length = len(que)
            for _ in range(length):
                el = que.popleft()
                for node in adj[el]:
                    indegree[node] -= 1
                    if indegree[node] == 0:
                        que.append(node)
        return ans
                