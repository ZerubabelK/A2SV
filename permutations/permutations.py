class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, path = []):
            if len(path) == len(nums):
                res.append([val for val in path])
                inPath.discard(nums[i])
                return path.pop()
            
            for j in range(len(nums)):
                if j != i and nums[j] not in inPath:
                    inPath.add(nums[j])
                    path.append(nums[j])
                    dfs(j, path)
                    
            if path:
                inPath.discard(nums[i])
                return path.pop()
                
        inPath = set()
        res = []
        dfs(-1)
        return res