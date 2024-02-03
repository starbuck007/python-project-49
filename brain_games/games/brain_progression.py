# Game: Arithmetic Progression
from random import randint


RULE = 'What number is missing in the progression?'


def get_arithmetic_progression() -> list[int]:
    """Get arithmetic progression"""
    start_progression = randint(1, 100)
    step_progression = randint(1, 10)
    arithmetic_progression = [start_progression + step_progression * i for i in range(10)]
    return arithmetic_progression


def get_correct_answer(arithmetic_progression: list, missing_number: int) -> str:
    """Get correct answer for question"""
    correct_answer = arithmetic_progression[missing_number - 1]
    return str(correct_answer)


def get_question() -> tuple[str, str]:
    """Get question and correct answer for game"""
    arithmetic_progression = get_arithmetic_progression()
    missing_number = randint(1, 10)
    question = [str(i) for i in arithmetic_progression]
    question[missing_number - 1] = '..'
    correct_answer = get_correct_answer(arithmetic_progression, missing_number)
    return ', '.join(question), correct_answer
