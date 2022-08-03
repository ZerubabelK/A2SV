# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        9,9,9,9,9,9,9 
        9,9,9,9
        8 9 9 9 0 0 1         
        '''
        def traverse(node1, node2, carry = 0):
            nonlocal head
            if not node1 and not node2:
                if carry > 0:
                    head.next = ListNode(carry)
                return
            add = carry
            if node1:
                add += node1.val
            if node2:
                add += node2.val
            
            head.next = ListNode(add % 10)
            head = head.next
            if node1 and node2:
                traverse(node1.next, node2.next, add // 10)
            elif node1:
                traverse(node1.next, None, add // 10)
            elif node2:
                traverse(None, node2.next, add // 10)
        dummy = head = ListNode()
        traverse(l1, l2)
        return dummy.next
        