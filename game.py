from player import Player
from deck import Deck
from card import suits , ranks, values
from card import Card

#Defines the players
player_one = Player('Player1')
player_two = Player('Player2')

#Creates a deck and shuffles it
new_deck = Deck()
new_deck.shuffle()

#Splits the deck of cards into two players
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# round_no for calculating no of rounds of the game
round_no = 0 
game_on = True

#game starts here
while game_on:
    round_no += 1
    print (f'Round {round_no}.')

    #Check if any player has no cards left with him.
    if len(player_one.all_cards) == 0:
        print("Player1 out of cards!! Player2 Wins!!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player2 out of cards!! Player1 Wins!!")
        game_on = False
        break

    #start a new round. Players drawing cards.
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    #At war( card value equals) condition
    at_war = True

    while at_war:
        #Checks the cards values of players and make a comparison
        if player_one_cards[-1].values > player_two_cards[-1].values:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif player_one_cards[-1].values < player_two_cards[-1].values:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        else:
            #card value equals and its war condition
            print("Its a War!!")

            #Check if the players have atleast 5 cards for war condition.

            if len(player_one.all_cards) < 5 :
                print("Player1 unable to declare war.")
                print("Player2 wins!!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5 :
                print("Player2 unable to declare war.")
                print("Player1 wins!!")
                game_on = False
                break

            else:
                #The game continues for war condition.
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())



