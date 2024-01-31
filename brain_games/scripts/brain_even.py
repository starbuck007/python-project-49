#!/usr/bin/env python3
import brain_games.brain_even as even


def main():
    print("Welcome to the Brain Games!")
    name = even.get_user_name()
    even.welcome_user(name)
    even.game(name)


if __name__ == '__main__':
    main()
