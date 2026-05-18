import unittest
from trie_model import build_trie_from_patterns, Trie

class TestTrieStructure(unittest.TestCase):

    def setUp(self):
        self.patterns = ["apple", "app", "apricot", "banana"]
        self.trie = build_trie_from_patterns(self.patterns)

    def test_search_existing_words(self):
        self.assertTrue(self.trie.search("apple"))
        self.assertTrue(self.trie.search("app"))
        self.assertTrue(self.trie.search("banana"))

    def test_search_non_existing_words(self):
        self.assertFalse(self.trie.search("orange"))
        self.assertFalse(self.trie.search("banan"))

    def test_starts_with_prefixes(self):
        self.assertTrue(self.trie.starts_with("app"))
        self.assertTrue(self.trie.starts_with("apr"))
        self.assertTrue(self.trie.starts_with("ban"))

    def test_starts_with_wrong_prefixes(self):
        self.assertFalse(self.trie.starts_with("cat"))
        self.assertFalse(self.trie.starts_with("bana-na"))

    def test_empty_trie(self):
        empty_trie = Trie()
        self.assertFalse(empty_trie.search("anything"))
        self.assertFalse(empty_trie.starts_with("any"))


if __name__ == "__main__":
    unittest.main()