# General logic for all brain games
import prompt


def welcome_user() -> str:
    """Greeting and get user's name"""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def check_answer(user_answer: str, correct_answer: str) -> bool:
    """Compare user's answer and correct answer"""
    return True if user_answer == correct_answer else False


def gameplay(game):
    """Core gameplay for all brain games"""
    counter = 0
    name = welcome_user()
    print(game.RULE)
    while counter < 3:
        question, correct_answer = game.get_question()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if check_answer(answer, correct_answer):
            counter += 1
            print('Correct!')

        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was"
                  f" '{str(correct_answer)}'\nLet's try again, {name}!")
            break
    if counter == 3:
        print(f'Congratulations, {name}!')
