import random


def generate_random_number(min, max):
    """
    The function generates a random integer between min and max.

    Args:
        min: The value of the lower bound for random number
        max: The value of the upper bound for the random number

    Returns:
        A random number is returned between min and max
    """
    return random.randint(min, max)


def choose_random_operator():
    """
    The function chooses for a randomly selected operator from +,- and *.
    """
    return random.choice(['+', '-', '*'])


def solve_problems(n1, n2, operator):
    """
    The function uses two variables and an operator to create equations between them.

    Args:
        n1: The first number
        n2: The second number
        operator: The operator

    Returns:
        The function returns the equaiton and the solution to the equation
    """
    equation = f"{n1} {operator} {n2}"
    solution = None

    if operator == '+':
        solution = n1 + n2
    elif operator == '-':
        solution = n1 - n2
    elif operator == '*':
        solution = n1 * n2
    else:
        return 'Operator has not been handled'
    return equation, solution

def math_quiz():
    s = 0
    t_q = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = generate_random_number(1, 10)
        n2 = generate_random_number(1, 5)
        operator = choose_random_operator()

        PROBLEM, ANSWER = solve_problems(n1, n2, operator)
        print(f"\nQuestion: {PROBLEM}")
        
        try:
            useranswer = int(input("Your answer: "))
        except ValueError:
            print("You did not enter a valid integer.")
            useranswer = -100000 #Assigned a value beyond our answers

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
