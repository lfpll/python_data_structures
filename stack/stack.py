class Stack:

    def __init__(self, max_size) -> None:
        if max_size <= 0:
            raise ValueError("Invalid max size for stack")
        self.max_size = max_size
        self.size = 0
        self.list = []
        
    
    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.max_size

    def push(self,value):
        if self.is_full():
            raise ValueError("The is stack is already full")
        self.size += 1
        self.list.append(value)

    def pop(self):
        if self.is_empty():
            raise ValueError("The list is empty")
        self.size -= 1
        return self.list.pop()

    def peek(self):
        if self.is_empty():
            raise ValueError("The list is empty")
        
        return self.list[-1]


    