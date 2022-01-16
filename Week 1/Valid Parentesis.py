class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(','{','[']
        closing = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        st = []
        if len(s)%2 != 0:
            return False
        for i in range(len(s)):
            if s[i] in set(opening):
                st.append(s[i])
            else:
                if i == 0:
                    return False
                if len(st) == 0:
                    return False
                else:
                    if st[-1] == closing[s[i]]:
                        st.pop()
                    else:
                        return False
        if len(st) == 0:
            return True
        else:
            return False
        print(st)
        