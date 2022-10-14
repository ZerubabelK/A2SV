# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            if curr.val == val:
                if prev:
                    tmp = curr.next
                    prev.next = tmp
                    curr.next = None
                    curr = tmp
                else:
                    tmp = curr.next
                    head = tmp
                    curr.next = None
                    curr = tmp
            else:
                prev = curr
                curr = curr.next
        return head
                    
            