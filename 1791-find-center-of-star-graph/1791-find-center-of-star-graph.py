class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        for key in adj:
            if len(adj[key]) == len(edges):
                return key
        