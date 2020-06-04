#!/usr/bin/env python3

'''Get better at no limit Texas hold'em.
'''

import argparse
import itertools
import time
import random
import numpy as np
import pandas as pd
#import holdem_calc
#from poker import Range
#from poker.hand import Combo
#import holdem_functions
from poker_trainer_functions import fold_or_raise, deal, get_high_score, update_high_score


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
    hand_rankings_file = 'poker_trainer.csv'
    hand_rankings = pd.read_csv(hand_rankings_file)

    # play the game
    high_score = get_high_score(high_score_file)
    input(f'The best time to get {points_required} points in a row is {high_score:.1f} seconds.\n'
           'Hit enter key to play.')
    start_time = time.time()
    while points < points_required:
        hand = random.sample(deck, hole_cards)
        seat = random.choice(seats)
        # optimal_action = get_answer(hand, seat, hand_rankings)  # TODO actually look up the correct value
        optimal_action = 'f'  # i.e. fold
        action = deal(hand, seat)
        if action == optimal_action:
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

# exit if you get ten right in a row
# save timer to file for best

# check if you should have folded either with a lookup table or monte carlo
# count outs
# calculate pot odds
# pin ranges
# keep a running score
#from poker import Range
#from poker.hand import Combo
#import holdem_functions
#odds = holdem_calc.calculate_odds_villan([], True, 1, None ,Combo('KsJc'), None, True, print_elapsed_time=True)
#print(odds)  # takes inf
