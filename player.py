#Player class defines the player information and contains functions for removing one card from the top,adding cards at the bottom.

class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        '''Removes one card object/card from the top of the deck'''
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        '''Adds new card/card objects to the bottom of the deck'''
        if type(new_cards) == type ([]):
            #list of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            #list of single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        '''Displays player information'''
        return f'Player {self.name} has {len(self.all_cards)} cards.'
