# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        nums = sorted([(i, num) for i, num in enumerate(nums)], key = lambda x: x[1])
        root = TreeNode(nums[-1][1]) 
        nodes = {}
        nodes[root] = nums[-1][0]
        for i in range(len(nums)-2, -1, -1):
            cur = root
            parent = None
            index, num = nums[i]
            while cur:
                node = TreeNode(num)
                nodes[node] = index
                if index < nodes[cur] and not cur.left:
                    cur.left = node
                    break
                elif index > nodes[cur] and not cur.right:
                    cur.right = node
                    break
                elif index > nodes[cur]:
                    cur = cur.right
                else:
                    cur = cur.left
        return root
                
            
            