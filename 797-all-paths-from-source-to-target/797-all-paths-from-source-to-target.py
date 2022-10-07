class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        def dfs(i, path):
            if i == len(graph)-1:
                res.append([n for n in path])
            for node in graph[i]:
                dfs(node, path + [node])
        dfs(0,[0])
        return res