class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, num * -1)
        if self.minheap and self.maxheap and self.heappeak(self.minheap) < self.heappeak(self.maxheap)*-1:
            val1 = heapq.heappop(self.maxheap)
            val2 = heapq.heappop(self.minheap)
            heapq.heappush(self.minheap, val1 * -1)
            heapq.heappush(self.maxheap, val2 * -1)
        if len(self.maxheap) > len(self.minheap) + 1:
            val = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, val * -1)
        elif len(self.minheap) > len(self.maxheap) + 1:
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, val * -1)

    def findMedian(self) -> float:
        if len(self.maxheap) == len(self.minheap):
            return (self.heappeak(self.maxheap)*-1 + self.heappeak(self.minheap))/2
        else:
            if self.maxheap and not self.minheap:
                return float(self.heappeak(self.maxheap)*-1)
            elif self.minheap and self.maxheap:
                val = min(self.heappeak(self.minheap), self.heappeak(self.maxheap) * -1)
                return float(val)
        
    def heappeak(self, heap):
        smallest = heapq.heappop(heap)
        heapq.heappush(heap, smallest)
        return smallest