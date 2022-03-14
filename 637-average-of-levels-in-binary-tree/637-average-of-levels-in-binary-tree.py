# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = collections.deque()
        visited = set()
        queue.append(root)
        visited.add(root)
        ans = []
        
        while queue:
            temp = []
            
            while queue:
                popped = queue.popleft()
                temp.append(popped)
                
            av = 0
            for node in temp:
                av += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(av/len(temp))
            temp = []
        
        return ans