import unittest
from euler import problem_1, problem_3, problem_9
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

class TestProblemThree(unittest.TestCase):
    def test_prime_number(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        answer = [False, True, True, False, True, False, True, False, False, False, True]
        result = []
        for d in data:
            result.append(problem_3.prime_number(d))
        self.assertEqual(result, answer)

class TestProblemNine(unittest.TestCase):
    def test_pythagorean(self):
        a = 3
        b = 4
        answer = 5
        result = problem_9.pythagorean(a, b)
        self.assertEqual(result, answer)

    def test_required_for_thousand(self):
        a = 3
        b = 4
        answer = 993
        result = problem_9.required_for_thousand(a, b)
        self.assertEqual(result, answer)

if __name__ == "__main__":
    unittest.main()