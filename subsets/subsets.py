class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, path = []):
            res.append([val for val in path])
            
            if len(path) == nums:
                return path.pop()
            
            for j in range(i + 1, len(nums)):
                path.append(nums[j])
                dfs(j, path)
            if path:
                return path.pop()
            
        res = []
        dfs(-1)
        return res