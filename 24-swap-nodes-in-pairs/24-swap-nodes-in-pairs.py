# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        if head.next == None:
            return head
        t = head.next
        def swap(head, prev):
            if head == None:
                return
            if head.next == None:
                return 
            tmp = head.next
            head.next = tmp.next
            tmp.next = head
            head = head.next
        
            if prev != None:
                prev.next = tmp
            prev = tmp.next
            swap(head, prev)
        swap(head, None)
        return t