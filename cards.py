import random
# Good morning!


class Card:
    def __init__(self):
        self.points = 300
        self.cards_num = 0

    def deal(self):
        self.cards_num = random.randint(1, 13)