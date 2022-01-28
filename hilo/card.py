import random


class Card:
    '''A card that show a random number on it.
    Attributes: random_card(int)'''

    def __init__(self):
        '''Constructs a new instance of Card.
        Arg: self'''
        # create a card object. This can be used for the current_card and next_card
        self.random_card = 0

    def draw(self):
        '''Draws a random card.
        Arg: self'''
        # The action of 'drawing' a new card
        # assign the card a random number between 1-13
        self.random_card = random.randint(1, 13)
