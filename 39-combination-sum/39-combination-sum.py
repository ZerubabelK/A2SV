class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        unique = set()
        def backtrack(i, path = [], tot = 0):
            if tot == target:
                unique.add(tuple((path)))
                return path.pop()
            
            for j in range(i, len(candidates)):
                if tot + candidates[j] > target:
                    continue
                path.append(candidates[j])
                backtrack(j, path, tot + candidates[j])
            if len(path) > 0:
                path.pop()
            return
        for i in range(len(candidates)):
            backtrack(i)
            
        return [list(el) for el in unique]