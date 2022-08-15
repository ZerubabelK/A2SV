"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque()
        if root:
            queue.append(root)
            
        while queue:
            length = len(queue)
            prev = Node()
            for i in range(length):
                node = queue.popleft()
                left, right = node.left, node.right
                if left and right:
                    prev.next = left
                    left.next = right
                    prev = right
                    queue.append(left)
                    queue.append(right)
                    
        return root
                    