# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nums = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.nums.append(node.val)
            inorder(node.right)
        inorder(root)
        self.index = -1

    def next(self) -> int:
        self.index += 1
        return self.nums[self.index]
        
    def hasNext(self) -> bool:
        return self.index + 1 < len(self.nums)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()