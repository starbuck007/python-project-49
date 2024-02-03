# Game: "Is It a Prime Number?"
from random import randint


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_correct_answer(number: int) -> str:
    """Get correct answer for question"""
    counter = 0
    for i in range(1, number + 1):
        if number % i == 0:
            counter += 1
            if counter > 2:
                break
    return 'yes' if counter == 2 else 'no'


def get_question() -> tuple[str, str]:
    """Get question and correct answer for game"""
    num = randint(0, 100)
    question = f'{str(num)}'
    correct_answer = get_correct_answer(num)
    return question, correct_answer
