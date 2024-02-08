#!/usr/bin/env python3
from brain_games.game_engine import play
from brain_games.games import brain_gcd


def main():
    play(brain_gcd)


if __name__ == '__main__':
    main()
