from hashmap.hashmap import HashTable
import pytest
class TestHashMap:

    def test_insert_search(self):
        table = HashTable()
        table.insert(key='1',value=5)
        assert table.search(key='1') == 5

    def test_is_in(self):
        table = HashTable()
        table.insert(key='1',value=5)
        assert table.search('1')
        assert not table.search('5')

    def test_delete(self):
        table = HashTable()
        table.insert(key='5',value=1)
        assert table.search(key='5')
        table.delete(key='5')
        assert not table.search(key='5')