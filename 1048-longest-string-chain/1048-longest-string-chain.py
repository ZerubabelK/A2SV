class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda word:len(word))
        print(words)
        @cache
        def dp(i):
            res = 0
            for j in range(i+1, len(words)):
                if self.checkIfPredecessor(words[i], words[j]):
                    res = max(res,dp(j))
            return res + 1
        ans = 0
        for i in range(len(words)):
            ans = max(ans, dp(i))

        return ans
    
    def checkIfPredecessor(self, word1, word2):
        wordSet2 = set(word2)
        if abs(len(word1) - len(word2)) != 1:
            return False
        i = j = 0
        count = 0
        while i < len(word1) and j < len(word2):
            if word1[i] == word2[j]:
                count += 1
                i += 1
                j += 1
            elif word1[i] in wordSet2:
                j += 1
            else:
                i += 1
                
        return count == min(len(word1), len(word2))