class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        inbound = lambda char: 65 <= ord(char) < 91 or 97 <= ord(char) < 123 or 48 <= ord(char) < 58
        equals = lambda char1, char2: str.lower(char1) == str.lower(char2)

        while left < right:
            rightChar = s[right]
            leftChar = s[left]
            
            if not inbound(leftChar):
                left += 1
                
            elif not inbound(rightChar):
                right -= 1

            elif equals(leftChar, rightChar):
                left += 1
                right -= 1
                continue
            else:
                return False
        
        return True
            
            
                