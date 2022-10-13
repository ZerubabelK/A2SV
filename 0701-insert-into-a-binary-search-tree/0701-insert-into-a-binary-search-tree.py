# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        par = None
        while node:
            par = node
            if node.val > val:
                node = node.left
            else:
                node = node.right
        if not par:
            return TreeNode(val)
        if par.val > val:
            par.left = TreeNode(val)
        else:
            par.right = TreeNode(val)
        return root