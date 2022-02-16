# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        i = 0
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        answer = [0 for i in range(length)]
        stack = []
        temp = head
        
        while temp:
            if len(stack) == 0:
                stack.append([i, temp.val])
            else:
                while stack and temp.val > stack[-1][1]:
                    popped = stack.pop()
                    answer[popped[0]] = temp.val
                stack.append([i, temp.val])
            i += 1
            temp = temp.next
        return answer