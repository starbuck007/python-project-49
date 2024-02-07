# General logic for all brain games
import prompt


def gameplay(game):
    """Core gameplay for all brain games"""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game.RULE)

    for i in range(3):
        question, correct_answer = game.get_question()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was"
                  f" '{str(correct_answer)}'\nLet's try again, {name}!")
            break
        else:
            print('Correct!')
    else:
        print(f'Congratulations, {name}!')
