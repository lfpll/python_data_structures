from stack.stack import Stack

class TestStack:

    def test_empty(self):
        tmp_stack = Stack(max_size=5)
        assert tmp_stack.is_empty()

    def test_full(self):
        tmp_stack = Stack(max_size=1)
        tmp_stack.push(1) 
        assert tmp_stack.is_full()

    def test_size(self):
        tmp_stack = Stack(max_size=4)
        tmp_stack.push(1)
        assert tmp_stack.size == 1
        tmp_stack.push(2)
        assert tmp_stack.size == 2
        tmp_stack.pop()
        assert tmp_stack.size == 1
        tmp_stack.pop()
        assert tmp_stack.size == 0

    def test_pop(self):
        tmp_stack = Stack(max_size=2)
        tmp_stack.push(1)
        assert tmp_stack.pop() == 1
        tmp_stack.push(4)
        assert tmp_stack.pop() == 4

    def test_push_peek(self):
        tmp_stack = Stack(max_size=2)
        tmp_stack.push(1)
        assert tmp_stack.peek() == 1
        tmp_stack.push(3)
        assert tmp_stack.peek() == 3
