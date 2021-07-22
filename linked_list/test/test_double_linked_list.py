from linked_list.double_linked_list import DoubleLinkedList


def test_append_empty():
    linked_list = DoubleLinkedList()
    linked_list.append(1)
    assert linked_list.tail.value == 1
    assert linked_list.head.value == 1

def test_three_appends():
    linked_list = DoubleLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    assert linked_list.tail.value == 3
    assert linked_list.head.value == 1
    assert linked_list.size == 3

def test_remove_one():
    linked_list = DoubleLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    assert linked_list.tail.previous.value == 2
    linked_list.remove_by_value(2)
    assert linked_list.tail.previous.value == 1
    linked_list.append(4)
    assert linked_list.tail.value == 4
    assert linked_list.size == 3
    assert linked_list.tail.previous.value == 3
