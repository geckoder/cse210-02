import random

class Card:

    def __init__(self):
        #create a card object. This can be used for the current_card and next_card
        
        self.value = 0
        #this makes it an integer

    def draw(self):
        #The action of 'drawing' a new card
        
        self.value = random.randint(1,13)
        #assign the card a random number of 1-13