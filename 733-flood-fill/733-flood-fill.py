class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        def dfs(row, col):
            image[row][col] = newColor
            visited.add((row, col))
            
            for d in DIR:
                new_row, new_col = row + d[0], col + d[1]
                if (new_row, new_col) in visited or not in_bound(new_row, new_col) or image[new_row][new_col] != start_color:
                    continue
                    
                dfs(new_row, new_col)
        
        in_bound = lambda row, col : 0 <= row < n and 0 <= col < m
        
        start_color = image[sr][sc]
        image[sr][sc] = newColor
        DIR = [[0,1],[1,0],[0,-1],[-1,0]]
        visited = set([(sr,sc)])
        dfs(sr, sc)
        return image