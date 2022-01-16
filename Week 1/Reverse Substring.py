class Solution:
    def reverseParentheses(self, s: str) -> str:
        tmp = []
        stack = []
        for i in range(len(s)):
            if s[i] != ")":
                stack.append(s[i])
            else:
                while stack[-1] != "(":
                    tmp.append(stack.pop())
                stack.pop()
                for i in tmp:
                    stack.append(i)
                tmp = []
        for i in range(len(stack)):
            tmp.append(stack[-1])
            stack.pop()
            
        newS = ""
        for i in range(len(tmp)):
            if tmp[-(i+1)] != ')' and tmp[-(i+1)] != '(':
                newS = newS + tmp[-(i+1)]
        return newS