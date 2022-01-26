import random


class Card:
    '''Attributes: card_num(int)'''

    def __init__(self):
        '''Constructs a new instance of Card.
        Arg: self'''
        # create a card object. This can be used for the current_card and next_card
        self.current_card = 0
        self.next_card = 0
        # this makes it an integer

    def draw(self):
        '''Draws a random card.
        Arg: self'''
        # The action of 'drawing' a new card
        # assign the card a random number of 1-13
        self.current_card = random.randint(1, 13)
        self.next_card = random.randint(1, 13)
