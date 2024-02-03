# Game: Find the greatest common divisor of given numbers
from random import randint


RULE = 'Find the greatest common divisor of given numbers.'


def get_correct_answer(numbers: list[int]) -> str:
    """Get correct answer for question"""
    correct_answer = 1
    numbers.sort()
    for i in range(1, numbers[0] + 1):
        if numbers[0] % i == 0 and numbers[1] % i == 0:
            correct_answer = i
        else:
            continue
    return str(correct_answer)


def get_question() -> tuple[str, str]:
    """Get question and correct answer for game"""
    nums = [randint(0, 100) for _ in range(2)]
    question = f'{str(nums[0])} {str(nums[1])}'
    correct_answer = get_correct_answer(nums)
    return question, correct_answer
