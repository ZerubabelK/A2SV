class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            ans = self.cache[key]
            del self.cache[key]
            self.cache[key] = ans
            return ans
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
            self.cache[key] = value
        elif self.capacity > len(self.cache):
            self.cache[key] = value
        elif self.capacity == len(self.cache):
            for i in self.cache:
                del self.cache[i]
                break
            self.cache[key] = value
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)