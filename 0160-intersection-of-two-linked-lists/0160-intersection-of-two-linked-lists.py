# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        while headA or headB:
            if headA in visited:
                return headA
            elif headB in visited or headA == headB:
                return headB
            if headA:
                visited.add(headA)
                headA = headA.next
            if headB:
                visited.add(headB)
                headB = headB.next
        return
                