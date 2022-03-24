# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        queue = collections.deque()
        
        if root:
            queue.append(root)
        
        while queue:
            ans.append(float('-inf'))
            length = len(queue)
            
            for i in range(length):
                node = queue.popleft()
                ans[-1] = max(ans[-1], node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return ans