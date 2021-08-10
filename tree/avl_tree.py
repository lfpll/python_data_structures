from tree.binary_search_tree import BinarySearchTree


class Node:
    left   = None
    right  = None
    height = 1
    
    def __init__(self,value) -> None:
        self.value = value


class AvlBinaryTree:

    def __init__(self):
        self.root = None

    def insert(self,value, node= None):
        # Case where root doens't exist 
        if not self.root:
            self.root = Node(value=value)
        else:
            # Right Insert
            if not node:
              return Node(value=value)
            elif value > node.value:
                node.right = self.insert(value=value,node=node.right)
            # Left Insert
            else:
                node.left =  self.insert(value=value,node=node.left)
            
            node.height = 1 + max(self.get_height(node.left),
                                self.get_height(node.right))

            balance: int = (self.get_height(node.right) - 
                                self.get_height(node.left))
                                
            # Right changes
            if balance  > 1:
                # Right rotation move
                if node.right.value < value:
                    return self.rotate_left(node)
                else:
                    node.right = self.rotate_right(node.right)
                    return self.rotate_left(node)
            # Left changes
            elif balance  < - 1:
                # Left rotation
                if node.left.value > value:
                    return self.rotate_right(node)
                else:
                    node.left = self.rotate_left(node.left)
                    return self.rotate_right(node)
            else:
                return node 
    
    def get_height(self,node) -> int:
        if node:
            return node.height
        return 0 

    def delete(self):
        pass

    def rotate_left(self, node: Node):
        tmp_node = Node(value=node.value)

        y = node.right
        left = y.left

        node.value = y.value
        node.left = tmp_node
        node.right = y.right
        tmp_node.right = left
        
        node.height     = 1 + max(self.get_height(node.left),
                                self.get_height(node.right))
        tmp_node.height = 1 + max(self.get_height(tmp_node.left),
                                self.get_height(tmp_node.right))

        return node

    def rotate_right(self, node: Node):
        tmp_node = Node(value=node.value)

        y = node.left
        right = y.right 
        
        node.value = y.value
        node.right = tmp_node
        node.left  = y.left
        tmp_node.left = right
        
        node.height     = 1 + max(self.get_height(node.left),
                                self.get_height(node.right))
        tmp_node.height = 1 + max(self.get_height(tmp_node.left),
                                self.get_height(tmp_node.right))
        
        return node