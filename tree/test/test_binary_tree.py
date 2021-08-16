from tree.binary_search_tree import BinarySearchTree
from tree.avl_tree import AvlBinaryTree
from tree.max_heap import MaxHeapArray
import pytest

class TestSearchBinaryTree:

    def test_insert(self):
        tree = BinarySearchTree()
        tree.insert(1)
        assert tree.root.value == 1

    def test_find(self):
        tree = BinarySearchTree()
        tree.insert(1)
        tree.insert(2)
        assert 2 == tree.find(2).value 
        
    def test_inexistend_value(self):
        tree = BinarySearchTree()
        tree.insert(1)
        with pytest.raises(ValueError) as error:
            tree.find(2)
            assert str(error.value) == ("Value %d is not in the binary tree.",2)

    def test_delete(self):
        tree = BinarySearchTree()
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
        tree = BinarySearchTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(7)
        tree.insert(3)
        tree.insert(15)
        tree.insert(13)
        tree.insert(17)
        assert [3,5,7,10,13,15,17] == tree.in_order_trav()


    def test_pre_order_trav(self):
        tree = BinarySearchTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(7)
        tree.insert(3)
        tree.insert(15)
        tree.insert(13)
        tree.insert(17)
        assert [10,5,3,7,15,13,17] == tree.pre_order_trav()
    


    def test_post_order_trav(self):
        tree = BinarySearchTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(7)
        tree.insert(3)
        tree.insert(15)
        tree.insert(13)
        tree.insert(17)
        assert [3,7,5,13,17,15,10] == tree.post_order_trav()


class TestAvlBinaryTree:
    

    def test_left_rotation(self):
        tree = AvlBinaryTree()
        tree.insert(20,tree.root)
        tree.insert(21,tree.root)
        tree.insert(22,tree.root)
        assert tree.root.value == 21
        assert tree.root.left.value == 20
        assert tree.root.right.value == 22

    def test_left_right_rotation(self):
        tree = AvlBinaryTree()
        tree.insert(10,tree.root)
        tree.insert(8,tree.root)
        tree.insert(9,tree.root)
        assert tree.root.value == 9
        assert tree.root.left.value == 8
        assert tree.root.right.value == 10

    def test_right_rotation(self):
        tree = AvlBinaryTree()
        tree.insert(10,tree.root)
        tree.insert(8,tree.root)
        tree.insert(7,tree.root)
        assert tree.root.value == 8
        assert tree.root.left.value == 7
        assert tree.root.right.value == 10


    def test_right_left_rotation(self):
        tree = AvlBinaryTree()
        tree.insert(20,tree.root)
        tree.insert(22,tree.root)
        tree.insert(21,tree.root)
        assert tree.root.value == 21
        assert tree.root.left.value == 20
        assert tree.root.right.value == 22


class TestMaxHeapArray:

    def test_pop(self):
        heap = MaxHeapArray()
        heap.insert(1)
        heap.insert(2)
        heap.insert(3)
        assert heap.pop() == 3


    def test_insert(self):
        heap = MaxHeapArray()
        heap.nodes = []
        heap.insert(1)
        heap.insert(2)
        heap.insert(3)
        assert heap.nodes == [3,2,1]

    def test_delete(self):
        heap = MaxHeapArray()
        heap.nodes = []
        heap.insert(1)
        heap.insert(2)
        heap.insert(3)
        heap.delete(1)
        assert heap.nodes[0] == 3
        assert heap.nodes[1] == 2
        heap.insert(5)
        assert heap.nodes[0] == 5
        assert heap.nodes[1] == 3
        assert heap.nodes[2] == 2
    
    def test_swap(self):
        heap = MaxHeapArray()
        heap.nodes = []
        heap.insert(1)
        heap.insert(2)
        heap.swap(0,1)
        assert heap.nodes[0] == 1
        assert heap.nodes[1] == 2

    def test_get_parent(self):
        heap = MaxHeapArray()
        heap.nodes = []
        heap.insert(1)
        heap.insert(3)
        heap.insert(2)
        assert heap.nodes[0] == 3
        assert heap.nodes[1] == 2
        assert heap.nodes[2] == 1
        assert heap.parent(1) == 3
    
    def test_left_child(self):
        heap = MaxHeapArray()
        heap.nodes = []
        heap.insert(1)
        heap.insert(3)
        heap.insert(2)
        assert heap.nodes[0] == 3
        assert heap.nodes[1] == 2
        assert heap.nodes[2] == 1
        assert heap.left_child_index(0) == 1

    def test_right_child(self):
        heap = MaxHeapArray()
        heap.nodes = []
        heap.insert(1)
        heap.insert(3)
        heap.insert(2)
        assert heap.nodes[0] == 3
        assert heap.nodes[1] == 2
        assert heap.nodes[2] == 1
        assert heap.right_child_index(0) == 2

    def test_multi_funs(self):
        heap = MaxHeapArray()
        heap.nodes = []
        heap.insert(1)
        heap.insert(2)
        heap.insert(3)
        heap.delete(1)
        
        assert heap.nodes[0] == 3
        assert heap.nodes[1] == 2
        assert heap.size == 2
        heap.insert(5)
        assert heap.nodes[0] == 5
        assert heap.pop() == 5
        heap.delete(3) 
        assert heap.pop() == 2
        