# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            dummy = TreeNode(val)
            root = dummy
            return root
        
        temp = root
        def dfs(root, val): 
            if not root.left and root.val > val:
                dummy = TreeNode(val)
                root.left = dummy
                return
            
            if not root.right and root.val < val:
                dummy = TreeNode(val)
                root.right = dummy
                return
            
            if root.val > val:
                self.insertIntoBST(root.left, val)
            else:
                self.insertIntoBST(root.right, val)
                
        dfs(temp, val)
        return root