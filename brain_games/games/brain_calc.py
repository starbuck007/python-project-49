# Game: Calculator
from random import choice, randint


RULE = 'What is the result of the expression?'


def calculate(number_1: int, number_2: int, operator: str) -> int:
    """Get correct answer for question"""
    if operator == '-':
        return number_1 - number_2
    elif operator == '+':
        return number_1 + number_2
    elif operator == '*':
        return number_1 * number_2


def get_content() -> tuple[str, str]:
    """Get question and correct answer for game"""
    number_1 = randint(0, 10)
    number_2 = randint(0, 10)
    operators = ['-', '+', '*']
    operator = choice(operators)
    question = f'{number_1} {operator} {number_2}'
    correct_answer = str(calculate(number_1, number_2, operator))
    return question, correct_answer
