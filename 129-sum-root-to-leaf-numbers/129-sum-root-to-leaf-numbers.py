# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def defs(root, res):
            if not root:
                return 0
            
            if not root.left and not root.right:
                res *= 10;
                res += root.val
                return res
            
            res *= 10;
            res += root.val
            return defs(root.left, res) + defs(root.right, res)
        
        return defs(root, 0)