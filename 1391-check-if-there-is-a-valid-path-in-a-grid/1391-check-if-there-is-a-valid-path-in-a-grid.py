class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        parent = {}
        rank = {}
        compliment = {1: [{},{3,5,1}], 2:[{2,5,6},{}],3:[{2,5,6},{}],4:[{5,6,2},{3,1,5}], 5: [{},{}], 6: [{}, {5,1,3}]}
        n, m = len(grid), len(grid[0])
        inbound = lambda r, c: 0 <= r < n and 0 <= c < m
        
        def find(x):
            if x not in parent:
                parent[x] = x
                rank[x] = 1
            if x == parent[x]:
                return x
            rep = find(parent[x])
            parent[x] = rep
            return rep
        
        def union(x, y):
            p_x = find(x)
            p_y = find(y)
            if p_x != p_y:
                if rank[p_x] > rank[p_y]:
                    parent[p_y] = p_x
                    rank[p_x] += rank[p_y]
                else:
                    parent[p_x] = p_y
                    rank[p_y] += rank[p_x]
                    
        for i in range(n):
            for j in range(m):
                rr, rc = i, j + 1
                dr, dc = i + 1, j
                if inbound(rr, rc) and grid[rr][rc] in compliment[grid[i][j]][1]:
                    union((i, j),(rr, rc))
                if inbound(dr, dc) and grid[dr][dc] in compliment[grid[i][j]][0]:
                    union((i, j), (dr, dc))
                    
        return find((0,0)) == find((n-1,m-1))