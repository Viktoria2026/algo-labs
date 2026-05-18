import unittest
from find_max_chain import find_max_chain

class TestWChain(unittest.TestCase):
    def test_example_1(self):
        words = ["crates", "car", "cats", "crate", "rate", "at", "ate", "tea", "rat", "a"]
        self.assertEqual(find_max_chain(words), 6)

    def test_example_2(self):
        words = ["b", "bcad", "bca", "bad", "bd"]
        self.assertEqual(find_max_chain(words), 4)

    def test_example_3(self):
        words = ["word", "anotherword", "yetanotherword"]
        self.assertEqual(find_max_chain(words), 1)

    def test_empty_list(self):
        self.assertEqual(find_max_chain([]), 0)

    def test_single_word(self):
        self.assertEqual(find_max_chain(["apple"]), 1)

    def test_disjoint_chains(self):
        words = ["a", "ab", "abc", "x", "xy"]
        self.assertEqual(find_max_chain(words), 3)

if __name__ == '__main__':
    unittest.main()