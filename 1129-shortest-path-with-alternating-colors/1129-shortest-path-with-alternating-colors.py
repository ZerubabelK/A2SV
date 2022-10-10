class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a, d in redEdges:
            adj[a].append((d, 'r'))
        for a, b in blueEdges:
            adj[a].append((b,'b'))
            
        queue = deque([(0, 'n')])
        res = [float('inf')] * n
        res[0] = 0
        dis = 1
        visited = set()
        while queue:
            length = len(queue)
            for _ in range(length):
                el = queue.popleft()
                visited.add(el)
                for node in adj[el[0]]:
                    if node in visited:
                        continue
                    if (el[1] == 'r' and node[1] == 'b') or (el[1] == 'b' and node[1] == 'r') or el[1] == 'n':
                        queue.append(node)
                        res[node[0]] = min(dis, res[node[0]])
            dis += 1
    
        for i in range(len(res)):
            if res[i] == float('inf'):
                res[i] = -1
        return res
            