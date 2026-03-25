import unittest
from quickselect import quickselect

class TestQuickSelect(unittest.TestCase):
    def test_normal_case(self):
        arr = [15, 7, 22, 9, 36, 2, 42, 18]
        value, index = quickselect(arr.copy(), 3)
        self.assertEqual(value, 22)

    def test_example(self):
        arr = [15, 7, 22, 9, 36, 2, 42, 18]
        k = 3
        value, index = quickselect(arr.copy(), k)
        self.assertEqual(value, 22)
        self.assertEqual(index, 2)

    def test_single_element(self):
        arr = [5]
        value, index = quickselect(arr.copy(), 1)
        self.assertEqual(value, 5)
        self.assertEqual(index, 0)

    def test_k_equals_length(self):
        arr = [4, 1, 7]
        value, index = quickselect(arr.copy(), 3)
        self.assertEqual(value, 1)

    def test_invalid_k(self):
        arr = [1, 2]
        with self.assertRaises(ValueError):
            quickselect(arr.copy(), 3)

if __name__ == "__main__":
    unittest.main()

