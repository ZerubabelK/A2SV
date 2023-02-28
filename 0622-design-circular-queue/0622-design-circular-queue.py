class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [None] * self.k
        self.rear, self.front = 0, 0

    def enQueue(self, value: int) -> bool:
        if self.queue[self.rear] == None:
            self.queue[self.rear] = value
            self.rear = self.next(self.rear)
            return True
        return False

    def deQueue(self) -> bool:
        if self.queue[self.front] == None: 
            return False
        self.queue[self.front] = None
        self.front = self.next(self.front)
        return True

    def Front(self) -> int:
        if self.queue[self.front] == None: 
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.queue[self.prev(self.rear)] == None: 
            return -1
        return self.queue[self.prev(self.rear)]

    def isEmpty(self) -> bool:
        if self.queue[self.front] == None and self.queue[self.rear] == None: 
            return True
        return False

    def isFull(self) -> bool:
        if self.queue[self.front] and self.queue[self.rear]: 
            return True
        return False

    def next(self, i: int) -> int:
        return 0 if i >= self.k-1 else i + 1

    def prev(self, i: int) -> int:
        return self.k-1 if i == 0 else i - 1

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()