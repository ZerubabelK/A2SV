class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        
        freq = [(-f[1], f[0]) for f in list(freq.items())]
        
        heapify(freq)
        
        return [heappop(freq)[1] for i in range(k)]