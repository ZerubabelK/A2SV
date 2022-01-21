class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1 = []
        st2 = []
        i = 0
        j = 0
        while i < len(s) or j < len(t):
            if i < len(s): 
                if s[i] != '#':
                    st1.append(s[i])
                if s[i] == '#' and i != 0 and len(st1) > 0:
                    st1.pop() 
            if j < len(t):
                if t[j] != '#':
                    st2.append(t[j])
                if t[j] == '#' and i != 0 and len(st2) > 0:
                    st2.pop()
            i += 1
            j += 1
        print(st1, st2)
        if ''.join(st1) == ''.join(st2):
            return True
        else:
            return False