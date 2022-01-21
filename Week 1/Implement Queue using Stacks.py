class MyQueue:

    def __init__(self):
        self.st1 = []

    def push(self, x: int) -> None:
        self.st1.append(x)
        
    def pop(self) -> int:    
        return self.st1.pop(0)

    def peek(self) -> int:
        return self.st1[0]

    def empty(self) -> bool:
        return len(self.st1) == 0