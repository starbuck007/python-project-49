# Game: "Is It a Prime Number?"
from random import randint
from math import sqrt


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    """Check number for prime"""
    if number <= 1:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def get_content() -> tuple[str, str]:
    """Get question and correct answer for game"""
    num = randint(0, 100)
    question = f'{num}'
    if is_prime(num):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
