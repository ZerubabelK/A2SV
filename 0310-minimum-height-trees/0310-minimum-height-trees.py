class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = defaultdict(list)
        indegree = [0 for i in range(n)]
        for a, b in edges:
            adj[a].append(b);adj[b].append(a)
            indegree[a] += 1;indegree[b] += 1
        que = deque()
        for i in range(len(indegree)):
            que.append(i) if indegree[i] == 1 else None
        res = []
        while que:
            level = []
            length = len(que)
            for _ in range(length):
                parent = que.popleft()
                for child in adj[parent]:
                    indegree[child] -= 1
                    if indegree[child] == 1:
                        que.append(child)
                level.append(parent)
                res = level
        return res