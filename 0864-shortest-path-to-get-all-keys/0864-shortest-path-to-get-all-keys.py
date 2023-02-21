class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        dist = collections.defaultdict(lambda: float("inf"))
        q = collections.deque()
        startr, startc = -1, -1
        
        n_keys = 0
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == "@":
                    startr = r
                    startc = c
                if grid[r][c].islower():
                    n_keys += 1
        q.append([startr, startc, 0])
        dist[(startr, startc, 0)] = 0
        
        def move(r, c, keys):
            if r < 0 or r >= nrow or c < 0 or c >= ncol:
                return []
            cell = grid[r][c]
            if cell == "#":
                return []
            if cell == "." or cell == "@":
                return [r, c, keys]
            if cell.islower():
                keys |= 1 << (ord(cell)-ord("a"))
                return [r, c, keys]
            if cell.isupper():
                if keys & (1 << (ord(cell)-ord("A"))):
                    return [r, c, keys]
                else:
                    return []
        
        final_keys = 2 ** n_keys - 1
        while q:
            r, c, keys = q.popleft()
            if keys == final_keys:
                return dist[(r, c, keys)]
            for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                state2 = move(r+dr, c+dc, keys)
                if not state2:
                    continue
                r2, c2, keys2 = state2
                if dist[(r2, c2, keys2)] > dist[(r, c, keys)] + 1:
                    dist[(r2, c2, keys2)] = dist[(r, c, keys)] + 1
                    q.append([r2, c2, keys2])
        return -1