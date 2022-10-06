class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        left, right = 0, len(self.timeMap[key])-1
        ans = ""
        while left <= right:
            mid = (left + right) // 2
            if self.timeMap[key][mid][1] > timestamp:
                right = mid - 1
            else:
                ans = self.timeMap[key][mid][0]
                left = mid + 1
        return ans
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)