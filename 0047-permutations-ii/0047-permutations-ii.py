class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(perm = [], visited = set()):
            if len(perm) == len(nums):
                if ''.join(list(map(str, perm))) not in visited:
                    ans.append(perm) 
                    visited.add(''.join(list(map(str, perm))))
                return 
            
            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    backtrack(perm + [nums[i]], visited)
                    visited.remove(i)
        ans = []
        backtrack()
        return ans