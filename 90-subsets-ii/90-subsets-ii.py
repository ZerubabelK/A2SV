class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        un = set()
        def backtrack(i, path):
            if tuple(path) not in un:            
                res.append(path)
                un.add(tuple(path))
            for j in range(i+1, len(nums)):
                backtrack(j, path + [nums[j]])
        for i in range(len(nums)):
            backtrack(i, [nums[i]])
        return res