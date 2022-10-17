class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        def dfs(n):
            val = n
            visited.add(n)
            for node in adj[n]:
                if node not in visited:
                    visited.add(node)
                    index = dfs(node)
                    val = index if quiet[index] < quiet[val] else val
                    
            return val
        
        adj = defaultdict(list)
        for a, b in richer:
            adj[b].append(a)
        answer = []
        visited = set()
        for i in range(len(quiet)):
            answer.append(dfs(i))
            visited.clear()
        return answer