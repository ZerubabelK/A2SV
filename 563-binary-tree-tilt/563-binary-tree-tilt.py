# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        s = [0]
        def dfs(root):        
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            val = root.val
            root.val = abs(left - right)
            s[0] += root.val
            
            return val + left + right
        
        dfs(root)
        
        return s[0]