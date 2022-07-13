class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        walls = set([tuple(wall) for wall in walls])
        guardSet = set([tuple(guard) for guard in guards])
        guarded = set()
        for x, y in guards:
            for i in range(y+1, n):
                if (x, i) in walls or (x, i) in guardSet:
                    break
                guarded.add((x, i))
                
            for i in range(y-1, -1, -1):
                if (x, i) in walls or (x, i) in guardSet:
                    break
                guarded.add((x, i))
                
            for i in range(x+1, m):
                if (i, y) in walls or (i, y) in guardSet:
                    break
                guarded.add((i, y))
            
            for i in range(x-1, -1, -1):
                if (i, y) in walls  or (i, y) in guardSet:
                    break
                guarded.add((i, y))
                
        return m * n - len(guarded) - len(guards) - len(walls)
        