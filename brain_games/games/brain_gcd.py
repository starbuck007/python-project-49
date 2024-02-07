# Game: Find the greatest common divisor of given numbers
from random import randint


RULE = 'Find the greatest common divisor of given numbers.'


def get_correct_answer(number_1: int, number_2: int) -> int:
    """Get correct answer for question"""
    correct_answer = 1
    min_number = min(number_1, number_2)
    for i in range(1, min_number + 1):
        if number_1 % i == 0 and number_2 % i == 0:
            correct_answer = i
        else:
            continue
    return correct_answer


def get_question() -> tuple[str, str]:
    """Get question and correct answer for game"""
    number_1 = randint(0, 100)
    number_2 = randint(0, 100)
    question = f'{str(number_1)} {str(number_2)}'
    correct_answer = str(get_correct_answer(number_1, number_2))
    return question, correct_answer
