# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr = []
        while head:
            arr.append(head)
            head = head.next
        p = dummy = ListNode(0)

        while len(arr) > 1:
            h = arr.pop(0)
            t = arr.pop()
            p.next = h
            h.next = t
            p = t
            p.next = None
        
        if arr: 
            p.next = arr.pop()
            p = p.next
            p.next = None
            
        return dummy.next