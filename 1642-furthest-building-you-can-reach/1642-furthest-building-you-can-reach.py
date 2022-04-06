class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        usedLadders = []
        n = len(heights)
        
        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                if ladders > 0:
                    heappush(usedLadders,diff)
                    ladders -= 1
                else:
                    heappush(usedLadders,diff)
                    bricks -= heappop(usedLadders)     
                    if bricks < 0:
                        return i
        return n - 1