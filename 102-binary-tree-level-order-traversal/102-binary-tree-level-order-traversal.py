# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if root:
            queue.append(root)
        ans = []
        while queue:
            level = []
            while queue:
                level.append(queue.popleft())
                
            for node in level:
                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
            ans.append([node.val for node in level])
        return ans
        