
class Node:
    def __init__(self,value):
        self.next = None
        self.previous = None
        self.value = value

class DoubleLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        
        new_node = Node(value)
        self.size +=  1

        # No nodes on the linked list
        if not self.head:
            self.head = self.tail = new_node
        else:
            # Adding using tail
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    
    def remove_by_value(self,value):
        current = self.head
        
        # Case that head is deleted
        if self.head.value == value:
            if self.size == 1:
                self.tail = None
            
            self.head = current.next
            self.head.previous = None
            self.size -= 1
            
        elif self.tail.value == value:
            # Case tail is deleted
            self.tail = self.tail.previous
            self.tail.next = None
            self.size -= 1
        else:
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                    current.next.previous = current
                    self.size -= 1
                    break
                else:
                    current = current.next


        