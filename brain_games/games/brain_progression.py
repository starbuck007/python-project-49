# Game: Arithmetic Progression
from random import randint


RULE = 'What number is missing in the progression?'


def get_arithmetic_progression() -> list[int]:
    """Get arithmetic progression"""
    start = randint(1, 100)
    step = randint(1, 10)
    progression = [start + step * i for i in range(10)]
    return progression


def get_correct_answer(progression: list, missing_number: int) -> str:
    """Get correct answer for question"""
    correct_answer = progression[missing_number - 1]
    return str(correct_answer)


def get_question() -> tuple[str, str]:
    """Get question and correct answer for game"""
    progression = get_arithmetic_progression()
    missing_number = randint(1, 10)
    question = [str(i) for i in progression]
    question[missing_number - 1] = '..'
    correct_answer = get_correct_answer(progression, missing_number)
    return ', '.join(question), correct_answer
