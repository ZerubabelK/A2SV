# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] += 1
        ans = [0]
        def dfs(node, _sum):
            if not node:
                return
            _sum += node.val
            ans[0] += prefix[_sum - targetSum]
            prefix[_sum] += 1
            dfs(node.left, _sum)
            dfs(node.right, _sum)
            prefix[_sum] -= 1
            return
        
        dfs(root, 0)
            
        return ans[0]
            