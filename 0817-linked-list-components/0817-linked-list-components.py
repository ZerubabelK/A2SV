# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        sets = set(nums)
        flag = False
        count = 0
        while head:
            if head.val in sets:
                flag = True
            else:
                count += 1 if flag else 0
                flag = False
            head = head.next
        count += 1 if flag else 0
        return count