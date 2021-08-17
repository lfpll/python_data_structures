class Node(dict):
    is_end_word: bool = False


class Trie:
    

    def __init__(self):
        self.root:dict = Node()

    def insert(self,word :str):
        # Get first node
        node = self.root
        
        # Insert letter by letter
        for l in word:
            if l not in node:
                node[l] = Node()
            node = node[l]
        
        # Last node is the end
        node.is_end_word = True


    def is_word(self,word :str):
        # Checks if word is valid
        
        node = self.root

        for l in word:
            if l not in node:
                return False
            node = node[l]

        return node.is_end_word