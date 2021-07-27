class Node:
    left = None
    right = None

    def __init__(self,value):
        self.value = value

class BinaryTree:

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

        if not node:
            return None
        if value > node.value:
            node.right = self.delete(value, node=node.right)
        elif value < node.value:               
            node.left = self.delete(value, node=node.left)
        else:
            if not node.right and not node.left:
                node = None
            elif not node.right:
                node.value = node.left.value
                node.left  = self.delete(value=node.value,
                                    node=node.left)
            elif not node.left:
                node.value = node.right.value
                node.right = self.delete(value=node.value,
                                    node=node.right)
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
        pass

    def pre_order_trav(self):
        pass

    def post_order_trav(self):
        pass

    def in_order_trav(self):
        pass