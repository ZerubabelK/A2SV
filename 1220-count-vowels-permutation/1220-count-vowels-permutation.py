class Solution:
    def countVowelPermutation(self, n: int) -> int:
        memo = {}
        def dp(node = 'r', length = 0):
            unique = 0
            if length == n:
                return 1
            if (length, node) in memo:
                return memo[(length, node)]
            
            if node == 'r':
                unique = dp('a', length + 1) + dp('e', length + 1) + dp('i', length + 1) + dp('o', length + 1) + dp('u', length + 1)
            elif node == 'a':
                unique = dp('e', length + 1)
            elif node == 'e':
                unique = dp('a', length + 1) + dp('i', length + 1)
            elif node == 'i':
                unique = dp('a', length + 1) + dp('e', length + 1) + dp('o', length + 1) + dp('u', length + 1)
            elif node == 'o':
                unique = dp('i', length + 1) + dp('u', length + 1)
            else:
                unique = dp('a', length + 1)
            memo[(length, node)] = unique
            return unique
        
        return dp('r') % (10 ** 9 + 7)
        
            