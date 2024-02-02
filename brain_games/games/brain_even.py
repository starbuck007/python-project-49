from random import randint


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_correct_answer(num):
    return 'yes' if num % 2 == 0 else 'no'


def get_question():
    num = randint(1, 100)
    question = f'{str(num)}'
    correct_answer = get_correct_answer(num)
    return question, correct_answer
