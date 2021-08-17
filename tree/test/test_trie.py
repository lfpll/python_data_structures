from tree.trie import Trie

class TestTrie:

    def test_insert(self):
        trie = Trie()
        trie.insert('humus')
        trie.insert('kibe')
        trie.insert('babaganoush')
        trie.insert('bolonha')
        trie.insert('kebab')
        trie.insert('falafel')
        assert 'u' in trie.root['h']
        assert 'm' in trie.root['h']['u']
        assert 'u' in trie.root['h']['u']['m']
        assert 's' in trie.root['h']['u']['m']['u']
        assert 'i' in trie.root['k']
        assert 'e' in trie.root['k']

    def test_is_word(self):
        trie = Trie()
        trie.root = dict()
        trie.insert('humus')
        trie.insert('humu')
        trie.insert('kibe')
        trie.insert('babaganoush')
        trie.insert('bolonha')
        trie.insert('kebab')
        trie.insert('falafel')
        assert trie.is_word('humu')
        assert trie.is_word('humus')
        assert not trie.is_word('hum')
