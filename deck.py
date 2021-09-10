# Deck class defines the deck of cards,creates card objects,shuffles the card_objects and pops one card from the deck.

import random
from card import suits , ranks, values
from card import Card

class Deck:
    def __init__(self):
        '''Created list of card objects'''
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card (suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        '''Shuffles the created card objects'''
        random.shuffle(self.all_cards)

    def deal_one(self):
        '''Pops out one card from the card objects deck'''
        return self.all_cards.pop()     