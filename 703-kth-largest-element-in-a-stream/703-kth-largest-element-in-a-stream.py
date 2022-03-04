from heapq import *
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums
        heapify(self.arr)
        
    def add(self, val: int) -> int:
        heappush(self.arr, val)
        
        while len(self.arr) > self.k:
            heappop(self.arr)
            
        return self.arr[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)