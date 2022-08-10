# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def func(left = 0, right = len(nums)):
            mid = (left + right) // 2
            if left < right:
                leftChild = func(left, mid)
                rightChild = func(mid + 1, right)
            else:
                return None
            
            curr = TreeNode(nums[mid])
            curr.left, curr.right = leftChild, rightChild
            return curr
        return func()