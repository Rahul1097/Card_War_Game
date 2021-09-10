#Card class contains the definition for suit, rank and value of the card

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King')

values = {'Ace':1,
          'Two':2,
          'Three':3,
          'Four':4,
          'Five':5,
          'Six':6,
          'Seven':7,
          'Eight':8,
          'Nine':9,
          'Ten':10,
          'Jack':11,
          'Queen':12,
          'King':13
          }

class Card:
    def __init__(self,suit,rank):
        '''Defines the suit, rank and values of card'''
        self.suit = suit
        self.rank = rank
        self.values = values[rank]

    def __str__(self):
        '''For storing the cards in deck as strings'''
        return self.rank + " of " +  self.suit
        