import random


class Card:
    '''Attributes: points(int), cards_num(int)'''

    def __init__(self):
        '''Constructs a new instance of Card.
        Arg: self'''
        self.points = 300
        self.cards_num = 0

    def deal(self):
        '''Draws a random card.
        Arg: self'''
        self.cards_num = random.randint(1, 13)
