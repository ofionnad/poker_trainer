#!/usr/bin/env python3

'''Functions for poker_trainer.py.
'''

import os
from colorama import Fore, Style


def fold_or_raise():
    '''Ask the player if they want to fold or raise.

    Returns
    -------
    string
        Decision to fold ('f') or raise ('r').
    '''
    action = input('Do you want to fold or raise? ')[0].lower()
    if action not in ['f', 'r']:
        print("I don't understand.")
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