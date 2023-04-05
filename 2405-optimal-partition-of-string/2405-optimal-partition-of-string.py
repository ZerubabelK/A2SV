class Solution:
    def partitionString(self, s: str) -> int:
        visited = 0
        count = 0
        isVisited = lambda ch, visited: visited & 1 << (ord(ch) - ord('a'))
        for ch in s:
            if isVisited(ch, visited):
                count += 1
                visited = 0
            visited = visited ^ 1 << (ord(ch) - ord('a'))
        return count + (1 if visited else 0)
                