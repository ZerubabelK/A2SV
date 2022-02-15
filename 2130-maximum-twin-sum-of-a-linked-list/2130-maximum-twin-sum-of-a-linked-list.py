# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        maxSum = 0
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        nextPtr = slow
        while prev and nextPtr:
            s = prev.val + nextPtr.val
            maxSum = max(s, maxSum)
            prev = prev.next
            nextPtr = nextPtr.next
        return maxSum