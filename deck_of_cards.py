import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd
from colorama import Fore, Style

class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def show(self):
        if self.suit=="\u2665":
            print(Fore.RED+"{}{}".format(self.number, self.suit))
        elif self.suit=="\u2666":
            print(Fore.GREEN+"{}{}".format(self.number, self.suit))
        elif self.suit=="\u2660":
            print(Fore.WHITE+"{}{}".format(self.number, self.suit))
        elif self.suit=="\u2663":
            print(Fore.BLUE+"{}{}".format(self.number, self.suit))


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["\u2665", "\u2666", "\u2660", "\u2663"]:
            for i in range(2,10):
                self.cards.append(Card(suit, i))
            for i in ['T', 'J', 'Q', 'K', 'A']:
                self.cards.append(Card(suit, i))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def deal_card(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.deal_card())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

class Game:
    def __init__(self, playerlist):
        """
        playerlist - list of player names
        """
        self.deck = Deck()
        self.deck.shuffle()
        self.nplayers = len(playerlist)
        self.playerlist = playerlist
        self.players = [Player(i) for i in self.playerlist]

    def start(self):
        for i in range(2):
            for i in self.players:
                i.draw(self.deck)

