# General logic for all brain games
import prompt


ROUND = 3


def play(game):
    """Core gameplay for all brain games"""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game.RULE)

    for i in range(ROUND):
        question, correct_answer = game.get_content()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was"
                  f" '{correct_answer}'\nLet's try again, {name}!")
            break
        else:
            print('Correct!')
    else:
        print(f'Congratulations, {name}!')
