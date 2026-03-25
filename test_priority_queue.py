import unittest
from avl_priority_queue import AVLPriorityQueue

class TestAVLQueue(unittest.TestCase):
    def setUp(self):
        self.pq = AVLPriorityQueue("test_log.txt")
        
    def test_logic(self):
        self.pq.insert("Task1", 10)
        self.pq.insert("Task2", 50)

        queue = self.pq.peek_queue()
        self.assertEqual(queue[0]['priority'], 50)
        self.assertEqual(queue[1]['priority'], 10)

        val, pri = self.pq.pop_highest_priority()
        self.assertEqual(val, "Task2")
        self.assertEqual(pri, 50)
    
    def test_duplicates(self):
        self.pq.insert("A", 20)
        self.pq.insert("B", 20)
        self.assertEqual(len(self.pq.peek_queue()), 2)

def run_app():
    pq = AVLPriorityQueue("user_actions.txt")
    
    while True:
        print("1. Вставити ")
        print("2. Видалити найпріоритетніший")
        print("3. Переглянути чергу")
        print("4. Запустити unittest")
        print("5. Вихід")
        
        choice = input("Дія: ")

        if choice == '1':
            val = input("Введіть назву елемента: ")
            try:
                pri = int(input("Введіть пріоритет (число): "))
                pq.insert(val, pri)
                print(f"Додано: {val}")
            except ValueError:
                print("Пріоритет має бути числом.")

        elif choice == '2':
            item = pq.pop_highest_priority()
            print(f"Вилучено: {item}" if item else "Черга порожня")

        elif choice == '3':
            items = pq.peek_queue()
            print("Черга:", items)

        elif choice == '4':
            print("запуск unittest")
            suite = unittest.TestLoader().loadTestsFromTestCase(TestAVLQueue)
            runner = unittest.TextTestRunner(verbosity=2)
            runner.run(suite)

        elif choice == '5':
            break

if __name__ == "__main__":
    run_app()