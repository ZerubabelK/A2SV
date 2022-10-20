class RandomizedSet:

    def __init__(self):
        self._dict = {}
        self._list = []

    def insert(self, val: int) -> bool:
        if val in self._dict:
            return False
        self._list.append(val)
        self._dict[val] = len(self._list)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self._dict:
            return False
        
        index = self._dict[val]
        self._list[index], self._list[-1] = self._list[-1], self._list[index]
        self._dict[self._list[index]] = index
        self._list.pop()
        del self._dict[val]
        return True

    def getRandom(self) -> int:
        r = randint(0, len(self._list)-1)
        return self._list[r]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()