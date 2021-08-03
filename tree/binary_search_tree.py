class Node:
    left = None
    right = None

    def __init__(self,value):
        self.value = value

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self,value, node= None):
        # Case where root doens't exist 
        if not self.root:
            self.root = Node(value=value)
        else:
            # first recursion
            if not node:
                node = self.root
            
            if value > node.value:
                if node.right:
                    return self.insert(value=value,node=node.right)
                else:
                    node.right = Node(value=value)
            elif value < node.value:
                if node.left:
                    return self.insert(value=value,node=node.left)
                else:
                    node.left = Node(value=value)
            else:
                raise ValueError("This value already exist's on tree")


    def delete(self,value,node=None):
        
        # Base case node is none
        if not node:
            return None

        # Go right if it's bigger
        if value > node.value:
            node.right = self.delete(value, node=node.right)
        # Go left if it's smaller
        elif value < node.value:               
            node.left = self.delete(value, node=node.left)
        # Value found
        else:
            # No Child
            if not node.right and not node.left:
                node = None
            # Single child on the left
            elif not node.right:
                node.value = node.left.value
                node.left  = self.delete(value=node.value,
                                    node=node.left)
            # Single child on the right
            elif not node.left:
                node.value = node.right.value
                node.right = self.delete(value=node.value,
                                    node=node.right)
            # Both childs
            else:
                tmp_node   = self.find_minimun(node.right)
                node.value = tmp_node.value
                node.right = self.delete(value=tmp_node.value,
                                            node=node.right)                
        return node


    def find_minimun(self,node):
        while node.left:
            node = node.left
        return node
        

    def find(self,value) -> bool:
        node = self.root
        while node and node.value != value:
            if node.value < value:
                node = node.right
            else:
                node = node.left

        # Node is none
        if not node:
            raise ValueError("Value %d is not in the binary tree.",value)

        return node

    def pre_order_trav(self, node: Node = None):
        if not node:
            node = self.root

        if node.left and node.right:
            return [node.value] + self.pre_order_trav(node=node.left) + self.pre_order_trav(node=node.right) 
        elif node.left: 
            return [node.value] + self.pre_order_trav(node=node.left) 
        elif node.right:
            return [node.value] + self.pre_order_trav(node=node.right)
        else:
            return [node.value]

    def post_order_trav(self,node: Node = None):
        if not node:
            node = self.root

        if node.left and node.right:
            return self.post_order_trav(node=node.left) + self.post_order_trav(node=node.right) +  [node.value]
        elif node.left: 
            return self.post_order_trav(node=node.left)   +  [node.value]
        elif node.right:
            return self.post_order_trav(node=node.right)  +  [node.value]
        else:
            return [node.value]

    def in_order_trav(self,node: Node = None):
        if not node:
            node = self.root

        if node.left and node.right:
            return self.in_order_trav(node=node.left) + [node.value] + self.in_order_trav(node=node.right) 
        elif node.left: 
            return self.in_order_trav(node=node.left) + [node.value]
        elif node.right:
            return self.in_order_trav(node=node.right) + [node.value]
        else:
            return [node.value]