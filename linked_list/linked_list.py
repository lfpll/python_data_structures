
class Node:
    def __init__(self,value):
        self.next = None
        self.value = value

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, value):
        
        new_node = Node(value)
        self.size +=  1

        # No nodes on the linked list
        if not self.head:
            self.head =  new_node
        else:
            # Iterating over linked list until is None
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def remove_by_value(self,value):
        current = self.head
        # Case that head is deleted
        if self.head.value == value:
            self.head = current.next
            return

        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                self.size -= 1
                break
            else:
                current = current.next


        