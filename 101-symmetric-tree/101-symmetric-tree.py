# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = root.left
        right = root.right
        # while left and right:
        #     if left.val != right.val:
        #         return False
        #     left = left.left
        #     right = right.right
        # return True     
        def symmetry(left, right):
            if left == None and right != None:
                return False
            if left != None and right == None:
                return False
            if left == None and right == None:
                return True
            
            if left.val == right.val:
                return symmetry(left.left, right.right) and symmetry(left.right, right.left)
            else:
                return False
        return symmetry(left, right)