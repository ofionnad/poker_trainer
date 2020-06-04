#!/usr/bin/env python3

'''Get better at no limit Texas hold'em.
'''

import argparse
import itertools
import time
import random
import numpy as np
from poker_trainer_functions import fold_or_raise, deal, get_answer, get_high_score, update_high_score


def main():
    '''Get better at no limit Texas hold'em.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--points_required', '-p', type=int, default=10,
                        help='Points required to win the game.')
    args = parser.parse_args()
    points_required = args.points_required

    # set up the game
    spades = '\u2660'  # ♠
    clubs = '\u2663'  # ♣
    hearts = '\u2665'  # ♥
    diamonds = '\u2666'  # ♦
    suits = [spades, clubs, hearts, diamonds]
    faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    deck = set(itertools.product(faces, suits))  # itertools.product() returns a generator
    seats = ['small blind', 'big blind', 'under the gun', 'under the gun +1',
             'under the gun +2', 'lojack', 'hijack', 'cutoff', 'button']
    hole_cards = 2
    points = 0
    high_score_file = 'poker_trainer_high_score.txt'

    # play the game
    high_score = get_high_score(high_score_file)
    input(f'The best time to get {points_required} points in a row is {high_score:.1f} seconds.\n'
           'Hit enter key to play.')
    start_time = time.time()
    while points < points_required:
        hand = random.sample(deck, hole_cards)
        seat = random.choice(seats)
        optimal_action = get_answer(hand, seat)
        action = deal(hand, seat)
        if action == 'q':
            exit()
        elif action == optimal_action:
            points += 1
            print(f'Points: {points}')
        else:
            print(f'Wrong! Points tally is back to zero.')
            points = 0
    score = time.time() - start_time
    if score < high_score:
        print(f'You got {points} points in {score:.1f} seconds. A new record!')
        update_high_score(score, high_score_file)
    else:
        print(f'You got {points} points in {score:.1f} seconds. The record remains {high_score:.1f} seconds.')


if __name__ == '__main__':
    main()
