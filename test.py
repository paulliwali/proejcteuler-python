import unittest

from euler import problem_1

class TestProblemOne(unittest.TestCase):
    def test_multiples_of_three_or_five(self):
        data = [1, 3, 5, 15, 20, 21, 23]
        answer = [False, True, True, True, True, True, False]
        result = []
        for d in data:
            result.append(problem_1.multiples_of_three_or_five(d))
        self.assertEqual(result, answer)
    
    def test_cumulative_sum(self):
        data = [10, 1000]
        answer = [23, 233168]
        result = []
        for d in data:
            result.append(problem_1.cumulative_sum(d))
        self.assertEqual(result, answer)

class TestProblemTwo(unittest.TestCase):
    def test

if __name__ == "__main__":
    unittest.main()