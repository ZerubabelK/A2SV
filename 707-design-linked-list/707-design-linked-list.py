class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        temp = self.head
        i = index - 1
        while i >= 0:
            temp = temp.next
            i -= 1
            
        return temp.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head
        self.head = node
        self.size +=1

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        if not self.head:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
        self.size +=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index > 0 and index < self.size:
            temp = self.head
            i = index - 1
            while i>0:
                temp = temp.next
                i -= 1
            node = ListNode(val)
            node.next = temp.next
            temp.next = node
            self.size +=1
        elif index == self.size:
            self.addAtTail(val)
        else:
            return

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        elif index == 0:
            node = self.head
            self.head = node.next
            del node
        else:
            temp = self.head 
            i = index - 1
            while i:
                temp = temp.next
                i -= 1
            node = temp.next
            temp.next = node.next
            del node
        self.size -=1
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)