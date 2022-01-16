class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        op = ['+', '-', '*', '/']
        for i in tokens:
            if i not in set(op):
                st.append(int(i))
            else:
                x = st.pop()
                y = st.pop()
                if i == '+': 
                    st.append(x + y)
                elif i == '-':
                    st.append(y - x)
                elif i == '*':               
                    st.append(x * y)
                else:
                    if x != 0:
                        st.append(int(y / x))
        return st[-1]