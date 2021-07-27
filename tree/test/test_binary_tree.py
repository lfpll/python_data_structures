from tree.binary_tree import BinaryTree
import pytest


class TestBinaryTree:

    def test_insert(self):
        tree = BinaryTree()
        tree.insert(1)
        assert tree.root.value == 1

    def test_find(self):
        tree = BinaryTree()
        tree.insert(1)
        tree.insert(2)
        assert 2 == tree.find(2).value 
        
    def test_inexistend_value(self):
        tree = BinaryTree()
        tree.insert(1)
        with pytest.raises(ValueError) as error:
            tree.find(2)
            assert str(error.value) == ("Value %d is not in the binary tree.",2)

    def test_delete(self):
        tree = BinaryTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(7)
        tree.insert(6)
        tree.insert(15)
        tree.insert(12)
        tree.insert(17)
        tree.insert(13)
        tree.delete(10,tree.root)

        # Test change root with both childs
        assert 12 == tree.root.value 

        # Test remove with None
        tree.delete(13,tree.root)
        assert tree.root.right.left is None

        # Test remove with only right child
        tree.delete(5,tree.root)
        assert tree.root.left.value == 7

        # Test remove with only left child
        tree.delete(7,tree.root)
        assert tree.root.left.value == 6

    
    
    def test_in_order_trav(self):
        tree = BinaryTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(7)
        tree.insert(3)
        tree.insert(15)
        tree.insert(13)
        tree.insert(17)
        assert [3,5,7,10,13,15,17] == tree.in_order_trav()


    def test_pre_order_trav(self):
        tree = BinaryTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(7)
        tree.insert(3)
        tree.insert(15)
        tree.insert(13)
        tree.insert(17)
        assert [10,5,3,7,15,13,17] == tree.pre_order_trav()
    


    def test_post_order_trav(self):
        tree = BinaryTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(7)
        tree.insert(3)
        tree.insert(15)
        tree.insert(13)
        tree.insert(17)
        assert [3,7,5,13,17,15,10] == tree.post_order_trav()
        