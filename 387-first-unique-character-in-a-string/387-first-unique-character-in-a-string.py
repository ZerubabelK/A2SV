class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        index = -1
        for i in range(len(s)):
            if freq[s[i]] == 1:
                index = i
                break
        return index