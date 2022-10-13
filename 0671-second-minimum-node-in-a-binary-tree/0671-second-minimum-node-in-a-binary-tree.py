# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node, val):
            if not node:
                return float('inf')
            if node.val > val:
                return node.val
            return min(dfs(node.left, val), dfs(node.right, val))
        ans = dfs(root, root.val)
        if ans == float('inf'):
            return -1
        return ans