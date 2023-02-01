class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        heap = []
        for i in range(len(growTime)):
            heappush(heap,(-growTime[i], plantTime[i]))
        cur = 0
        ans = 0
        while heap:
            grow, plant = heappop(heap)
            ans = max(cur + (-grow) + plant, ans)
            cur += plant
            
        return ans