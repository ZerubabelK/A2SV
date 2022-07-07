class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
            hash = {}
            numOfSubs = 0
            for i in range(len(words)):
                j = 0
                z = 0
                if words[i] in hash:
                    if hash[words[i]]:
                        numOfSubs += 1
                    continue
                        
                while j < len(words[i]) and z < len(s):
                    if words[i][j] == s[z]:
                        j += 1
                        z += 1
                    else:
                        z += 1
                if j == len(words[i]):
                    hash[words[i]] = True
                    numOfSubs += 1
                else:
                    hash[words[i]] = False
            return numOfSubs