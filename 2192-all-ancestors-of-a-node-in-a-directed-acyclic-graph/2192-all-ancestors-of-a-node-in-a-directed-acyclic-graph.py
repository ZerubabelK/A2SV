from sortedcontainers import SortedSet
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        indegree = [0] * n
        for a, b in edges:
            adj[a].append(b)
            indegree[b] += 1
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        ans = defaultdict(SortedSet)
        while queue:
            el = queue.popleft()
            for child in adj[el]:
                ans[child].add(el)
                ans[child].update(ans[el])
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        res = [[] for i in range(n)]
        for key in ans:
            res[key] = list(ans[key])
        return res
                
                