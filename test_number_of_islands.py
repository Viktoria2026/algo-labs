import unittest
import os
from number_of_islands import count_islands

class TestIslandCounter(unittest.TestCase):
    
    def test_main_grid(self):

        grid = [
            [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
            [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 1, 1, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 1, 1, 1, 1]
        ]
        self.assertEqual(count_islands(grid), 9)

    def test_small_islands(self):
        grid = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
        self.assertEqual(count_islands(grid), 5)

def run_file_io():
    """Читає input.txt та записує в output.txt."""
    if not os.path.exists("input.txt"):
        print("\n[!] Помилка: Файл input.txt не знайдено.")
        return
    grid = []
    with open("input.txt", "r") as f:
        for line in f:
            if line.strip():
                grid.append(list(map(int, line.split())))
                
    result = count_islands(grid)

    with open("output.txt", "w") as f:
        f.write(str(result))
    
    print(f"\n результат ({result}) записано у файл output.txt")

if __name__ == "__main__":
    unittest.main(exit=False)
    run_file_io()