class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        if not n % 2 == 0:
            arr.append(0)
        _id = 1
        while len(arr) < n:
            arr.append(_id)
            arr.append(_id * -1)
            _id += 1
        return arr