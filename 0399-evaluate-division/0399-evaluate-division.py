class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1 / values[i]))
            
        result = [-1.0] * len(queries)
        
        def dfs(i, node, dist, target):
            if node ==  target:
                result[i] = dist
                return
            visited.add(node)
            for neighbor, length in graph[node]:
                if neighbor not in visited:
                    dfs(i, neighbor, dist * length, target)
                    
        for i, (u,v) in enumerate(queries):
            visited = set()
            if u in graph:
                dfs(i, u, 1.0, v)
                
        return result