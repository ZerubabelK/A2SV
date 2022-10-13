# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev, head = None, node
        while head.next:
            head.next.val, head.val = head.val, head.next.val
            prev = head
            head = head.next
        prev.next = None
        
            