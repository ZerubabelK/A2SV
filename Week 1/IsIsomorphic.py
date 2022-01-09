class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return self.halfIsom(s, t) and self.halfIsom(t, s)

    def halfIsom(self, s, t):
        check = {}
        for i in range(len(s)):
            if s[i] not in check:
                check[s[i]] = t[i]
            elif check[s[i]] != t[i]:
                return False
        return True