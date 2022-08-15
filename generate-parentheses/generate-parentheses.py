class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        options = ['(', ')']
        def dfs(opening, closing, path = []):
            if opening == 0 and closing == 0:
                res.append(''.join(path))
                return path.pop()
            
            if opening > 0:
                path.append('(')
                dfs(opening - 1, closing, path)
                
            if closing > 0 and opening < closing:
                path.append(')')
                dfs(opening, closing - 1, path)
            
            if path:
                path.pop()
            return 
                
        res = []
        dfs(n, n)
        return res
    