# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        return max(self.dfs(root, True), self.dfs(root, False))
    
    @cache
    def dfs(self, node, offset):
        if not node:
            return 0
        res = None
        if offset:
            res = self.dfs(node.right, False) + self.dfs(node.left, False) + node.val
        else:
            res = max(self.dfs(node.right, False), self.dfs(node.right, True)) + max(self.dfs(node.left, False), self.dfs(node.left, True))
        return res
        
        