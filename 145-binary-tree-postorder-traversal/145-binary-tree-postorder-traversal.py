# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def inorder(root,arr):
            if root == None:
                return
            
            inorder(root.left, arr)
            inorder(root.right,arr)
            arr.append(root.val)
            
        inorder(root, arr)
        
        return arr