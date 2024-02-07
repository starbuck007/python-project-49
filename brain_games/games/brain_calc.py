# Game: Calculator
import random


RULE = 'What is the result of the expression?'


def calculate(number_1: int, number_2: int, operator: str) -> int:
    """Get correct answer for question"""
    if operator == '-':
        return number_1 - number_2
    elif operator == '+':
        return number_1 + number_2
    else:
        return number_1 * number_2


def get_question() -> tuple[str, str]:
    """Get question and correct answer for game"""
    number_1 = random.randint(0, 10)
    number_2 = random.randint(0, 10)
    operators = ['-', '+', '*']
    operator = random.choice(operators)
    question = f'{str(number_1)} {operator} {str(number_2)}'
    correct_answer = str(calculate(number_1, number_2, operator))
    return question, correct_answer
