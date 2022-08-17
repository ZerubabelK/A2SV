class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        DIR = [(0,1), (1,0), (0,-1), (-1,0)]
        n, m = len(matrix), len(matrix[0])
        visited, ans = set(), []
        i, j, d = 0, 0, 0
        inbound = lambda row, col: 0 <= row < n and 0 <= col < m

        while len(visited) < n * m:
            if (i,j) not in visited:
                ans.append(matrix[i][j])
            visited.add((i,j))
            
            if inbound(i + DIR[d][0],j + DIR[d][1]) and (i + DIR[d][0],j + DIR[d][1]) not in visited:
                i += DIR[d][0]
                j += DIR[d][1]
            
            else:
                if d < len(DIR) - 1:
                    d += 1
                else:
                    d = 0
                    
        return ans