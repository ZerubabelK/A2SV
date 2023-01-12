class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for x,y, dist in roads:
            graph[x].append((y,dist))
            graph[y].append((x,dist))
        

        ans = [float('inf')]
        visited = {1}
    
        def dfs(root, next_dist):
            for child,dist in graph[root]:
                ans[0] = min(ans[0], dist)
                if child not in visited:
                        visited.add(child)
                        dfs(child, dist)
                        
        dfs(1, float('inf'))
        return ans[0]
