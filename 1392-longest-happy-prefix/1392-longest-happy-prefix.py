class Solution:
    def longestPrefix(self, s: str) -> str:
        length = self.findLPS(s)[-1]
        return s[:length]
    
    def findLPS(self, s):
        n = len(s)
        i, j = 0, 1
        LPS = [0] * n
        while j < n:
            if s[i] == s[j]:
                LPS[j] = i + 1
                i += 1
                j += 1
            elif i == 0: 
                LPS[j] = 0
                j += 1
            else:
                i = LPS[i-1]
        return LPS