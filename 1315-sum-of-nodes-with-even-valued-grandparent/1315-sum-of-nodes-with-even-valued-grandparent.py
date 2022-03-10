# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        def dfs(root, P = None, GP = None,  sumOfNodes = 0):
            if not root:
                return sumOfNodes
            
            if GP and GP.val % 2 == 0:
                sumOfNodes += root.val

            sumOfNodes += dfs(root.left, root, P) + dfs(root.right, root, P)
            
            return sumOfNodes
        
        return dfs(root) 