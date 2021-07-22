from linked_list.linked_list import LinkedList

def test_append():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    assert linked_list.head.value == 1

def test_delete():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.remove_by_value(1)
    assert linked_list.head == None

def test_delete_by_value():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(3)
    linked_list.append(2)
    assert linked_list.size == 3

