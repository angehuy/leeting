# Run in terminal to test: python -m unittest test_solution.py
import unittest
from smallestMissingNum import solution  # Replace `your_solution_file` with the name of your Python file.

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(solution([3, 4, -1, 1]), 2)  # Expected output: 2

    def test_case_2(self):
        self.assertEqual(solution([1, 2, 3]), 4)  # Expected output: 4

    def test_case_3(self):
        self.assertEqual(solution([-1, -3]), 1)  # Expected output: 1

    def test_case_4(self):
        self.assertEqual(solution([0, -2, 1, 2, 5]), 3)  # Expected output: 3

    def test_case_5(self):
        self.assertEqual(solution([]), 1)  # Empty list, expected output: 1

    def test_case_6(self):
        self.assertEqual(solution([7, 8, 9, 11, 12]), 1)  # Expected output: 1

    def test_case_7(self):
        self.assertEqual(solution([1]), 2)  # Single element (1), expected output: 2

    def test_case_8(self):
        self.assertEqual(solution([2]), 1)  # Single element (2), expected output: 1

if __name__ == "__main__":
    unittest.main()
