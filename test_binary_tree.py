import unittest
import os
from binary_tree import BinaryTree, build_tree

class TestBinaryTreeDiameter(unittest.TestCase):
    def test_single_node(self):
        root = BinaryTree(1)
        self.assertEqual(root.get_diameter(), 0)
    def test_complex_tree(self):
        nodes = [1, 3, 2, 7, 4]
        root = build_tree(nodes)
        self.assertEqual(root.get_diameter(), 3)
def run_file_processing():
    input_file = "input.txt"
    output_file = "result.txt"
    if not os.path.exists(input_file):
        with open(input_file, "w") as f:
            f.write("1 3 2 7 4 None None 8")
        print(f"Створено тестовий файл: {input_file}")

    try:
        with open(input_file, "r") as f:
            raw_data = f.read().split()
            data = [int(x) if x.lower() != "none" else None for x in raw_data]
        root = build_tree(data)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("--- Результати обробки бінарного дерева ---\n")
            f.write("Прямий обхід (Pre-order):\n")
            root.print_traversals()
            diameter = root.get_diameter()
            f.write(f"\n\nДіаметр дерева: {diameter}\n")
        print(f"Обробка завершена. Результат у '{output_file}'")
    except Exception as e:
        print(f"Помилка при роботі з файлами: {e}")

if __name__ == "__main__":
    run_file_processing()
    print("\nЗапуск юніт-тестів:")
    unittest.main()
    