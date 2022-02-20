class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        i = 0
        j = 0
        while j < len(s):
            if s[j] in set(s[i:j]):
                i += 1
            else:
                j += 1
            maxLength = max(maxLength, j - i)
        return maxLength