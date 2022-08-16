class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        freq = []
        repeat = 0
        for ch in s:
            if ch.isdigit():
                repeat = repeat * 10 + int(ch)
            elif ch != ']':
                if repeat:
                    freq.append(repeat)
                    repeat = 0
                st.append(ch)
            else:
                tmp = []
                while st[-1] != '[':
                    tmp.append(st.pop())
                st.pop()
                dec = freq.pop()
                val = ''.join(tmp[::-1])
                tmp = []
                for i in range(dec):
                    tmp.append(val)
                st.append(''.join(tmp))
        
        return ''.join(st)
                
                