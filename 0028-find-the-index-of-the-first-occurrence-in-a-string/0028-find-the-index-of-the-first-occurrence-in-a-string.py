class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        patternLPS = self.computeLPSArray(needle)
        n, m = len(needle), len(haystack)
        i, j = 0, 0
        while i < n and j < m:
            if haystack[j] == needle[i]:
                i += 1
                j += 1
            elif i != 0:
                i = patternLPS[i-1]
            else:
                j += 1
        return j - n if i >= n else -1
            
        
    def computeLPSArray(self, pattern):
        n = len(pattern)
        LPS = [0] * n
        i, j = 0, 1
        
        while j < n:
            if pattern[i] == pattern[j]:
                i += 1
                LPS[j] = i
                j += 1
            elif i != 0:
                i = LPS[i-1]
            else:
                LPS[j] = 0
                j += 1
        return LPS