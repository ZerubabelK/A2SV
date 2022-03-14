# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        if root:
            queue.append(root)
        arr = []
        level = 0
        while queue:
            temp = []
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                temp.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                    
            if level % 2 == 0:
                arr.append(temp[::-1])
            else:
                arr.append(temp)
                
            level += 1
            temp = []
            
        return arr
        