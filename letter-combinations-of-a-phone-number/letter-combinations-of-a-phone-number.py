class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        adj = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        
        def dfs(i, path = [], depth = len(digits)):
            if depth == 0:
                if path:
                    res.append(''.join(path))
                    path.pop()
                return
            
            for j in range(i+1, len(digits)):
                for child in adj[digits[j]]:
                    path.append(child)
                    dfs(j, path, depth - 1)
            if path:
                return path.pop()
        
        res = []
        dfs(-1)
        return res
            
                  
        