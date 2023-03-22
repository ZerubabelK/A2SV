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
    def connect(self, root: 'Node') -> 'Node':
        queue = deque([root] if root else [])
        while queue:
            length = len(queue)
            prev = None
            for _ in range(length):
                node = queue.popleft()
                left, right = node.left, node.right
                if prev:
                    prev.next = left if left else right
                if left:
                    left.next = right
                    prev = left if not right else right
                if right:
                    prev = right
                queue.append(left) if left else None
                queue.append(right) if right else None
                
        return root
                