# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self,root, d):
            
            if root == None:
                return 0
                       
            if root.left == None and root.right == None:
                return d
            
            return max(self.depth(root.left, d + 1), self.depth(root.right, d + 1))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        if abs(self.depth(root.left, 1) - self.depth(root.right, 1)) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)