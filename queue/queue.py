
class Queue:
    
    def __init__(self,size):
        self.size    = size
        self.queue   = [None]*size
        self.rear    = size - 1
        self.front   = self.current_size = 0

    def is_empty(self) -> bool:
        return self.current_size == 0
    
    def is_full(self) -> bool:
        return self.current_size == self.size

    def peek_bottom(self) -> int:
        return self.queue[self.rear]

    def enqueue(self,value):
        if self.is_full():
            raise Exception("Queue is already full.")
        self.rear = (self.rear + 1 )% self.size
        self.queue[self.rear] = value
        self.current_size += 1
        

    def dequeue(self) -> int:        
        if self.is_empty():
            raise Exception("Queue is empty")
        self.current_size -= 1
        item = self.queue[self.front]
        self.front = (self.front + 1 ) % self.size
        return item

    def peek(self) -> int:
        return self.queue[self.front]

