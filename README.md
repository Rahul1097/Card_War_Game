# Card_War_Game
Card War Game demonstrating simple Python OOPs concepts.

<img src = "https://github.com/Rahul1097/Card_War_Game/blob/master/images/image1.PNG" width=100%>

<img src = "https://github.com/Rahul1097/Card_War_Game/blob/master/images/image2.PNG" width=100%>

# Game Description-

The objective of the game is to win all of the cards.

The deck is divided evenly among the players, giving each a down stack. In unison, each player reveals the top card of their deck — this is a "battle" —and the player with the higher card takes both of the cards played and moves them to their stack.

If the two cards played are of equal value, then there is a "War".Both players place the next 5 cards face down and then another card face-up. The owner of the higher face-up card wins the war and adds all the cards on the table to the bottom of their deck. If the face-up cards are again equal then the battle repeats with another set of face-down/up cards. This repeats until one player's face-up card is higher than their opponent's.

Reference - https://en.wikipedia.org/wiki/War_(card_game)

# The code contains 3 classes-

1. **Class Card** contains the definition for suit, rank and value of the card.
2. **Class Deck** defines the deck of cards, creates card objects, shuffles the card objects and pops one card from the deck.
3. **Class Player** defines the player information and contains functions for removing one card from the top, adding cards at the bottom.

**The Game logic includes-**
1. The no of rounds for which the game lasted.
2. If any player ends up with all his cards, game ends and other player wins.
3. War condition if the cards match up, with atleast 5 cards left with the players to play the war.
4. Game ends if any player does not have sufficient cards to play the war.

# Steps to Setup-

Clone the repository and run below command-

```python game.py```
