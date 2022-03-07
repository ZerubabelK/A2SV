# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode()
        head = dummy
        heap = [[lists[i].val, i] for i in range(len(lists)) if lists[i]]
        heapify(heap)
        cnt = 0
        
        while heap:
            
            minval = heappop(heap)
            j = minval[1]
            lists[j] = lists[j].next
            
            if lists[j] != None:
                heappush(heap, [lists[j].val, j])
            else:
                cnt += 1
                
            node = ListNode(minval[0])
            dummy.next = node
            dummy = node
            
            if cnt == len(lists):
                break
                
        return head.next   