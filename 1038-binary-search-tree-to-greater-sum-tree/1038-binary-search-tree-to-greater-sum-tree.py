# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node, prev):
            if not node:
                return prev
            s = dfs(node.right, prev) + node.val
            node.val = s
            l = dfs(node.left, s)
            
            return l
        head = root
        dfs(root,0)
        return head