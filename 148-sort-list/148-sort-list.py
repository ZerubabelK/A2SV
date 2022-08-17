# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        arr.sort()
        dummy = ListNode()
        root = dummy
        for val in arr:
            dummy.next = ListNode(val)
            dummy = dummy.next
        
        return root.next