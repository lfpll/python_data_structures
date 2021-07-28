from queue.queue import Queue
import pytest

class TestQueueOperations:
    
    def test_enqueue(self):
        queue = Queue(size=5)
        queue.enqueue(5)
        assert queue.peek() == 5
        queue.enqueue(3)
        assert queue.peek_bottom() == 3

    def test_dequeue(self):
        queue = Queue(size=5)
        queue.enqueue(5)
        queue.enqueue(3)
        queue.enqueue(2)
        queue.enqueue(1)
        queue.enqueue(4)
        assert queue.dequeue() == 5
        queue.enqueue(6)
        assert queue.dequeue() == 3
        assert queue.dequeue() == 2
        assert queue.dequeue() == 1
        assert queue.dequeue() == 4
        assert queue.dequeue() == 6

    def test_peek(self):
        queue = Queue(size=5)
        queue.enqueue(5)
        assert queue.peek() == 5
        queue.enqueue(3)
        assert queue.peek() == 5
        queue.dequeue()
        assert queue.peek() == 3

    def test_is_empty(self):
        queue = Queue(size=5)
        assert queue.is_empty()
        queue.enqueue(5)
        assert not queue.is_empty()
        queue.dequeue() 
        assert queue.is_empty()

    def test_is_full(self):
        queue = Queue(size=5)
        assert not queue.is_full()
        queue.enqueue(5)
        queue.enqueue(5)
        queue.enqueue(5)
        queue.enqueue(5)
        queue.enqueue(5)
        assert queue.is_full()
        queue.dequeue()
        assert not queue.is_full()

class TestQueueErrors:
    
    def test_max_capacity(self):
        queue = Queue(size=5)
        queue.enqueue(5)
        queue.enqueue(5)
        queue.enqueue(5)
        queue.enqueue(5)
        queue.enqueue(5)
        with pytest.raises(Exception) as error:
            queue.enqueue(5)
            assert str(error.value) == "Queue is already full."

    def test_dequeue_empty(self):
        queue = Queue(size=5)
        with pytest.raises(Exception) as error:
            queue.dequeue()
            assert str(error.value) == "Queue is empty."

