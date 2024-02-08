# Game: Even or Not
from random import randint


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_content() -> tuple[str, str]:
    """Get question and correct answer for game"""
    num = randint(1, 100)
    question = f'{num}'
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
