class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        for a, b in edges:
            if a not in indegree: indegree[a] = 0
            indegree[b] += 1
        return [key for key in indegree if indegree[key] == 0]