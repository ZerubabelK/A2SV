class DetectSquares:

    def __init__(self):
        self.pointsMap = defaultdict(int)
        
    def add(self, point: List[int]) -> None:
        self.pointsMap[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        count = 0
        
        for x, y in self.pointsMap:
            
            if x == point[0] or y == point[1] or abs(x - point[0]) != abs(y - point[1]):
                continue
            if (x, point[1]) in self.pointsMap and (point[0], y) in self.pointsMap:
                count += self.pointsMap[(x, point[1])] * self.pointsMap[(point[0], y)] * self.pointsMap[(x, y)]
                
        return count


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)