# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        def depth(root, d):
            
            if root == None:
                return float('inf')
                       
            if root.left == None and root.right == None:
                return d
            
            return min(depth(root.left, d + 1), depth(root.right, d + 1))
        
        return depth(root, 1)   