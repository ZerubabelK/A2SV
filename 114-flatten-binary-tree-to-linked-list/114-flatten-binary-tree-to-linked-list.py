# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        prev = TreeNode()
        def prefix(node):
            nonlocal prev
            
            if not node:
                return 
            left, right = node.left, node.right
            prev.right, prev.left = node, None
            prev = prev.right
            prefix(left)
            prefix(right)
            
        prefix(root)    
        