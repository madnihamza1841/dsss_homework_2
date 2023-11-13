import unittest
from math_quiz import generate_random_number, choose_random_operator, solve_problems


class TestMathGame(unittest.TestCase):
    """
    Class for test cases for math quiz helper functions.
    """
    
    def test_generate_random_number(self):
        """
        Tests that the random number generated is within the bounds set
        """
        min = 1
        max = 10

        for i in range (10000):
            number = generate_random_number(min, max)
            self.assertTrue(min <=number <=max)

    def test_choose_random_operator(self):
        """
        Tests that a randomly chosen operator exists from +, - and *
        """
        operators = ['+','-', '*']
        
        for i in range(10000):
            operator = choose_random_operator()
            self.assertTrue(operator in operators)

    def test_solve_problems(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (7, 3, '-', '7 - 3', 4),
                (6, 4, '*', '6 * 4', 24),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = solve_problems(num1, num2, operator)
                self.assertTrue(problem == expected_problem)
                self.assertTrue(answer == expected_answer)


if __name__ == "__main__":
    unittest.main()
