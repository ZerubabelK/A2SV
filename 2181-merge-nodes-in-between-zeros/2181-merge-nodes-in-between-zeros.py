# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = dummy = ListNode()
        head = head.next
        cur = 0
        while head:
            if head.val:
                cur += head.val
            else:
                node = ListNode(cur)
                dummy.next = node
                dummy = node
                cur = 0
            head = head.next
            
        return start.next
            