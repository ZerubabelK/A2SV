# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, Up = float('inf'), Lo = -float('inf')):
            if not node:
                return True
            if node.val >= Up or node.val <= Lo:
                return False
            return dfs(node.left, node.val, Lo) and dfs(node.right, Up, node.val)
        return dfs(root)
            