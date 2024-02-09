# Game: Find the greatest common divisor of given numbers
from random import randint


RULE = 'Find the greatest common divisor of given numbers.'


def get_divisor(number_1: int, number_2: int) -> int:
    """Get the greatest common divisor of numbers"""
    correct_answer = 1
    min_number = min(number_1, number_2)
    for i in range(1, min_number + 1):
        if number_1 % i == 0 and number_2 % i == 0:
            correct_answer = i
    return correct_answer


def get_content() -> tuple[str, str]:
    """Get question and correct answer for game"""
    number_1 = randint(0, 100)
    number_2 = randint(0, 100)
    question = f'{number_1} {number_2}'
    correct_answer = str(get_divisor(number_1, number_2))
    return question, correct_answer
