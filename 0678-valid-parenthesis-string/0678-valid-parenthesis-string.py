class Solution:
    def checkValidString(self, s: str) -> bool:
        stack, stars = [], []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == "*":
                stars.append(i)
            else:
                if len(stack) > 0:
                    stack.pop()
                elif len(stars) > 0:
                    stars.pop()
                else:
                    return False
                
        while len(stack) > 0:
            if len(stars) > 0:
                if stars[-1] < stack[-1]:
                    return False
                else:
                    stars.pop()
                    stack.pop()
            else:
                return False

        return len(stack) == 0