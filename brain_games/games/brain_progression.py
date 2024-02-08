# Game: Arithmetic Progression
from random import randint

RULE = 'What number is missing in the progression?'


def get_arithmetic_progression() -> list[int]:
    """Get arithmetic progression"""
    progression_length = 10
    start = randint(1, 100)
    step = randint(1, 10)
    end = start + (step * progression_length)
    progression = list(range(start, end, step))
    return progression


def get_content() -> tuple[str, str]:
    """Get question and correct answer for game"""
    progression = get_arithmetic_progression()
    missing_index = randint(1, 10)
    correct_answer = str(progression[missing_index - 1])
    progression_str = [str(i) for i in progression]
    progression_str[missing_index - 1] = '..'
    question = ' '.join(progression_str)
    return question, correct_answer
