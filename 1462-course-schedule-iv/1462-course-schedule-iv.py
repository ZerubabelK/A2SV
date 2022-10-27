class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj_matrix = [[0 for _ in range(numCourses)] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj_matrix[a][b] = 1
            
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    adj_matrix[i][j] |= adj_matrix[i][k] and adj_matrix[k][j]
        
        ans = []
        for u, v in queries:
            if adj_matrix[u][v]:
                ans.append(True)
            else:
                ans.append(False)
                
        return ans