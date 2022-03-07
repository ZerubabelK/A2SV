class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = [(-f[1], f[0]) for f in list(Counter(words).items())]
        
        heapify(freq)
        
        return [heappop(freq)[1] for i in range(k)]