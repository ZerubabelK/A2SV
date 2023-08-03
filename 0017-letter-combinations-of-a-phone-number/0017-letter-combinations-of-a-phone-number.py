class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        def backtrack(i, strs):
            if i >= len(digits):
                ans.append(''.join(strs))
                return
            
            for ch in mapping[digits[i]]:
                backtrack(i+1, strs + [ch])
        ans = []
        backtrack(0, []) if digits else None
        return ans