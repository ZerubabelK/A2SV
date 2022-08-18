class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        slopes = defaultdict(int)
        
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                slope = self.findSlope(points[i], points[j])
                slopes[(points[i][0], points[i][1], slope)] += 1
                
        _max = 0
        
        for key in slopes:
            _max = max(_max, slopes[key])
            
        return _max + 1
        
        
    def findSlope(self, point1, point2):
        if point2[0] - point1[0] != 0:
            return (point2[1] - point1[1]) / (point2[0] - point1[0])
        else:
            return float('inf')