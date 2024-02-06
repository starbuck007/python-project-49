# Game: "Is It a Prime Number?"
from random import randint
from math import sqrt


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_correct_answer(number: int) -> str:
    """Get correct answer for question"""
    if number <= 1:
        return 'no'
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return 'no'
    return 'yes'


def get_question() -> tuple[str, str]:
    """Get question and correct answer for game"""
    num = randint(0, 100)
    question = f'{str(num)}'
    correct_answer = get_correct_answer(num)
    return question, correct_answer
