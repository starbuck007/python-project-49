# Game: Even or Not
from random import randint


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_correct_answer(num: int) -> str:
    """Get correct answer for question"""
    return 'yes' if num % 2 == 0 else 'no'


def get_question() -> tuple[str, str]:
    """Get question and correct answer for game"""
    num = randint(1, 100)
    question = f'{str(num)}'
    correct_answer = get_correct_answer(num)
    return question, correct_answer
