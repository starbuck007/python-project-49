# Game: Get the result of the expression
import random


RULE = 'What is the result of the expression?'


def get_correct_answer(numbers: list[int], operator: str) -> str:
    """Get correct answer for question"""
    if operator == '-':
        return str(numbers[0] - numbers[1])
    elif operator == '+':
        return str(numbers[0] + numbers[1])
    else:
        return str(numbers[0] * numbers[1])


def get_question() -> tuple[str, str]:
    """Get question and correct answer for game"""
    nums = [random.randint(0, 10) for _ in range(2)]
    operators = ['-', '+', '*']
    operator = random.choice(operators)
    question = f'{str(nums[0])} {operator} {str(nums[1])}'
    correct_answer = get_correct_answer(nums, operator)
    return question, correct_answer
