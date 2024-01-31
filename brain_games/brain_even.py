from random import randint
import prompt


def get_user_name():
    name = prompt.string('May I have your name? ')
    return name


def welcome_user(name):
    print(f'Hello, {name}')


def is_even(num):
    return 'yes' if num % 2 == 0 else 'no'


def game(name):
    counter = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while counter < 3:
        num = randint(1, 100)
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')

        if answer == is_even(num):
            counter += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was"
                  f" '{is_even(num)}'\nLet's try again!")
            break
    if counter == 3:
        print(f'Congratulations, {name}!')
