class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        provinces = 0
        
        def dfs(node, matrix):
            visited.add(node)
        
            for j in range(len(matrix[node])):
                if j not in visited and matrix[node][j] != 0:
                    dfs(j, matrix)
                    
        for i in range(len(isConnected)):
            if i not in visited:
                provinces += 1
            dfs(i, isConnected)
            
        return provinces