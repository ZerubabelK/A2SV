class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
        items = sorted(freq.items(), key = lambda x: x[1])
        setCnt, n = 0, len(arr)
        for i in range(-1, -1 - len(items), -1):
            setCnt += 1
            n -= items[i][1]
            if n <= len(arr) / 2:
                return setCnt