#!/usr/bin/env python3

'''Functions for poker_trainer.py.
'''

import os
import pandas as pd
from colorama import Fore, Style


def fold_or_raise():
    '''Ask the player if they want to fold or raise.

    Returns
    -------
    string
        Decision to fold ('f') or raise ('r').
    '''
    action = input('Do you want to fold or raise? ')[0].lower()
    if action not in ['f', 'r', 'q']:
        print("I don't understand. (q to quit)")
        fold_or_raise()
    return action


def deal(hand, position='button'):
    '''Deal cards to terminal.

    Parameters
    ----------
    hand : list
        Two cards being dealt.
    position : string, optional
        Seat at the table (default = 'button').

    Returns
    -------
    string
        Whether to fold or not.
    '''
    spades = '\u2660'  # ♠
    clubs = '\u2663'  # ♣
    hearts = '\u2665'  # ♥
    diamonds = '\u2666'  # ♦
    colour = {spades: Fore.BLACK, clubs: Fore.GREEN, hearts: Fore.RED, diamonds: Fore.BLUE}
    cards_with_colour = []
    for card in hand:
        cards_with_colour.extend([colour[card[1]], *card, Style.RESET_ALL])
    print("You're dealt\t{}{}{}{}\t{}{}{}{}\t(position: {})".format(*cards_with_colour, position))
    return fold_or_raise()


def get_answer(hand, position, hand_rankings_file='poker_trainer.csv'):
    '''Given a hand, determine whether it is optimal to raise or fold.
    '''
    hand_rankings = pd.read_csv(hand_rankings_file)
    short_hand_1 = hand[0][0] + hand[1][0]
    short_hand_2 = hand[1][0] + hand[0][0]  # either card can be first
    if hand[0][1] == hand[1][1]:
        short_hand_1 += 's'  # suited
        short_hand_2 += 's'  # suited
    if (short_hand_1 not in list(hand_rankings['hand']) and
        short_hand_2 not in list(hand_rankings['hand'])):
        return 'f'
    elif short_hand_1 in list(hand_rankings['hand']):
        return list(hand_rankings[hand_rankings['hand'] == short_hand_1][position])[0]
    else:  # short_hand_2 in list(hand_rankings['hand'])
        return list(hand_rankings[hand_rankings['hand'] == short_hand_2][position])[0]


def get_high_score(high_score_file):
    '''Read the best time score from a file or set it to the maximum allowed value
    if the file does not exist.

    Parameters
    ----------
    high_score_file : string
        Filename containing the high score.

    Returns
    -------
    float
        The best time score.
    '''
    if os.path.isfile(high_score_file):
        with open(high_score_file) as f:
            for score in f:
                high_score = float(score)
    else:
        high_score = 999  # sys.float_info.max
    return high_score


def update_high_score(score, high_score_file):
    '''Save the score to file if it is a new record.

    '''
    with open(high_score_file, 'w') as f:
        f.write(str(score))
