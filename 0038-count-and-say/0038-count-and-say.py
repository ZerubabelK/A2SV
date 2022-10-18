class Solution:
    def countAndSay(self, n: int) -> str:
        current = '1'
        for i in range(1, n):
            pairs = self.findPairs(current)
            current = self.mergePairs(pairs)
        return current
    
    def findPairs(self, digits: str) -> list:
        result = []
        
        freq = 1
        digit_length = len(digits)
        for i in range(digit_length):
            if i == digit_length - 1:
                result.append([digits[i], freq])
            elif digits[i] == digits[i+1]:
                freq += 1
            else:
                result.append([digits[i], freq])
                freq = 1
                
        return result
    
    def mergePairs(self, pairs):
        result = ''
        for pair in pairs:
            result += str(pair[1]) + pair[0]
        return result