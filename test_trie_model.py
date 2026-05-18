import unittest
from trie_model import build_trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = build_trie(["apple", "app", "application", "banana"])
    
    def test_search(self):
        self.assertTrue(self.trie.search("apple"))
        self.assertTrue(self.trie.search("app"))
        self.assertFalse(self.trie.search("ap"))
        self.assertFalse(self.trie.search("orange"))
    
    def test_starts_with(self):
        self.assertTrue(self.trie.starts_with("app"))
        self.assertTrue(self.trie.starts_with("ban"))
        self.assertFalse(self.trie.starts_with("bat"))
        self.assertFalse(self.trie.starts_with("xyz"))
    
    def test_insert_then_search(self):
        self.assertFalse(self.trie.search("orange"))
        self.trie.insert("orange")
        self.assertTrue(self.trie.search("orange"))
        self.assertTrue(self.trie.starts_with("or"))
    
    def test_empty_trie(self):
        empty_trie = build_trie([])
        self.assertFalse(empty_trie.search("anything"))
        self.assertFalse(empty_trie.starts_with("a"))

if __name__ == "__main__":
    unittest.main()