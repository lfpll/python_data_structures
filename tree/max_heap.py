class Node:
    left   = None
    right  = None
    weight = 1
    
    def __init__(self,value) -> None:
        self.value = value

class MaxHeapArray:

    nodes: list = []
    size: int   = 0
    def __init__(self) -> None:
        pass

    def insert(self,value):
        
        #  Inserting value
        self.size += 1
        self.nodes.append(value)

        if self.size > 1:
            # Check if it's bigger
            index = self.size - 1

            # Check if parent and 
            while self.has_parent(index) and self.parent(index) < value:
                self.swap(self.get_parent_index(index),index)
                index = self.get_parent_index(index)
                
    
    
    def parent(self,index):
        return self.nodes[self.get_parent_index(index)]

    def has_parent(self,index):
        return index > 0

    def get_parent_index(self,index):
        if index == 0: 
            return -1
        
        p_index = int(index/2)
        return p_index


    def swap(self,index,swap_index):
        # Storing to swap on list
        tmp = self.nodes[index]
        self.nodes[index] = self.nodes[swap_index]
        self.nodes[swap_index] = tmp


    def heapifyDown(self,index):
        # Check if there is left child and 
        while self.has_left_child(index):
            left  = self.left_child_index(index)
            right = self.right_child_index(index)

            # Move right tree 
            if self.has_right_child(index) and self.nodes[right] > self.nodes[left]: 
                self.swap(right,index)
                index = right
            # Move Left tree
            else:
                self.swap(left,index)
                index = left

    def delete(self,value:int):
                
        if self.size > 1:
            # Check if it's bigger
            index = self.nodes.index(value)

            # Swapping by the last one and deleting value
            self.swap(index,self.size - 1)
            self.nodes.pop()
            self.heapifyDown(index)

            #  Inserting value
            self.size -= 1

    def pop(self):
        self.swap(0,self.size - 1)
        val = self.nodes.pop()
    
        self.heapifyDown(0)
        self.size -= 1
        return val
        
    
    def has_left_child(self,index):
        l = self.left_child_index(index)
        if l:
            return self.size - 1 <= self.left_child_index(index)
        else: 
            return False
    
    def has_right_child(self,index):
        
        r = self.right_child_index(index)
        if r:
            return self.size -1 <= self.right_child_index(index)
        else: 
            return False
    
    def left_child_index(self,index):
        l = int(index)*2 +1
        if self.size - 1 >= l:
            return l            
    
    def right_child_index(self,index):
        r = int(index)*2 + 2
        if self.size - 1 <= r:
            return r            
