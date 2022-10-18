# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.dfs(root, None)
    
    def dfs(self, current_node, previous_node):
        if not current_node:
            return previous_node
        
        left_child = current_node.left
        right_child = current_node.right
        
        if previous_node:
            previous_node.right = current_node
        current_node.left = None
            
        left_previous_node = self.dfs(left_child, current_node)
        right_previous_node = self.dfs(right_child, left_previous_node)
        
        return right_previous_node