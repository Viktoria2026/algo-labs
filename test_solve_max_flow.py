import unittest
import os
from solve_max_flow import solve_max_flow

class TestFlowerLogistics(unittest.TestCase):
    
    def setUp(self):
        self.test_file = "temp_test_roads.csv"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_simple_straight_flow(self):
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write("F1\nS1\nF1,S1,10\n")
            
        flow, _, _ = solve_max_flow(self.test_file)
        self.assertEqual(flow, 10)

    def test_bottleneck_road(self):
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write("F1\nS1\nF1,X1,15\nX1,X2,5\nX2,S1,12\n")
            
        flow, _, _ = solve_max_flow(self.test_file)
        self.assertEqual(flow, 5)

    def test_multiple_farms_and_shops(self):
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write("F1,F2\nS1,S2\nF1,X1,10\nF2,X1,10\nX1,S1,8\nX1,S2,7\n")
            
        flow, _, _ = solve_max_flow(self.test_file)
        self.assertEqual(flow, 15)

    def test_disconnected_network(self):
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write("F1\nS1\nF1,X1,10\nX2,S1,10\n")
            
        flow, _, _ = solve_max_flow(self.test_file)
        self.assertEqual(flow, 0)

if __name__ == "__main__":
    unittest.main()