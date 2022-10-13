# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        def dfs(node, s = 0):
            nonlocal ans
            if not node:
                return s
            left = dfs(node.left, s)
            if left + 1 == k:
                ans = node.val
            right = dfs(node.right, left + 1)
            
            return right
        dfs(root)
        return ans