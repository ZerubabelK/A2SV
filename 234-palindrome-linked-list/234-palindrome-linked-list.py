# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        result = True
        prev = None
        fast = head
        slow = head
        length = 0
        while head:
            length += 1
            head = head.next
            
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        if length%2 != 0:
            slow = slow.next
        while prev and slow:
            if prev.val != slow.val:
                result = False
            prev = prev.next
            slow = slow.next
            
        return result