import unittest
import os
from selection_sort import aggressive_cows, read_from_file

class TestCows(unittest.TestCase):
    
    def setUp(self):
        self.filename = "temp_input.txt"
        with open(self.filename, "w") as f:
            f.write("5 3\n1 2 8 4 9")

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_logic_from_example(self):
        stalls = [1, 2, 8, 4, 9]
        self.assertEqual(aggressive_cows(stalls, 3), 3)

    def test_file_reading(self):
        data = read_from_file(self.filename)
        self.assertIsNotNone(data)
        n, c, stalls = data
        self.assertEqual(aggressive_cows(stalls, c), 3)

    def test_two_cows_only(self):
        stalls = [1, 10, 100]
        self.assertEqual(aggressive_cows(stalls, 2), 99)

if __name__ == "__main__":
    filename = "input.txt"
    
    with open(filename, "w") as f:
        f.write("5 3\n1 2 8 4 9")

    os.startfile(filename) 
    data = read_from_file(filename)
    n_val, c_val = 5, 3 
    sections_val = [1, 2, 8, 4, 9] 
    print(f"Максимальна мінімальна відстань: {aggressive_cows(sections_val, c_val)}")
    unittest.main()

