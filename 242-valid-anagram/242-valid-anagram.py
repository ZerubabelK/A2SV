class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        _freq = defaultdict(int)
        for l in s:
            _freq[l] += 1
        
        for l in t:
            if l not in _freq:
                return False
            _freq[l] -= 1
        
        for key in _freq:
            if _freq[key] != 0:
                return False
            
        return True