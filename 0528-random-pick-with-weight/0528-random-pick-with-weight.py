class Solution:

    def __init__(self, w: List[int]):
        s = sum(w)
        self.w = w
        self.weights = [weig/s for weig in w]
        self.indices = defaultdict(list)
        for i in range(len(w)):
            self.indices[w[i]].append(i)
            
    def pickIndex(self) -> int:
        val = random.choices(self.w, self.weights)
        return self.indices[val[0]][math.ceil(random.random() * len(self.indices[val[0]]))-1]
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()