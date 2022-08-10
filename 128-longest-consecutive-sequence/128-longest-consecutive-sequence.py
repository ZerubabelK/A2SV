class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        graph = {}
        
        for num in nums:
            graph[num] = num + 1
        
        def traverse(node):
            depth = 0
            if node not in graph:
                return 0
            if node in memo:
                return memo[node]
            
            depth += traverse(graph[node])
            
            memo[node] = depth + 1
            
            return depth + 1
        
        memo = {}
        ans = 0
        
        for key in graph:
            depth = traverse(key)
            ans = max(ans, depth)
  
        return ans
        
            