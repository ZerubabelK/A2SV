class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        
        def alter(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
                    
        while l < r:
            if s[l] != s[r]:
                return alter(l+1,r) or alter(l, r-1)
            l += 1
            r -= 1
        return True