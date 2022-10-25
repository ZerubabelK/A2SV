class Solution:
    def longestPrefix(self, s: str) -> str:
        length = self.computeLPSArray(s, len(s))[-1]
        return s[:length]
    
    def computeLPSArray(self, pat, M):
        j = 0

        lps = [0] * M
        i = 1

        while i < M:
            if pat[i]== pat[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps