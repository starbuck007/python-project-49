import random


RULE = 'What is the result of the expression?'


def get_correct_answer(numbers, operator):
    if operator == '-':
        return numbers[0] - numbers[1]
    elif operator == '+':
        return numbers[0] + numbers[1]
    else:
        return numbers[0] * numbers[1]


def get_question():
    nums = [random.randint(0, 10) for _ in range(2)]
    operators = ['-', '+', '*']
    operator = random.choice(operators)
    question = f'{str(nums[0])} {operator} {str(nums[1])}'
    correct_answer = str(get_correct_answer(nums, operator))
    return question, correct_answer
