from hilo.card import Card

class Director:

    def __init__(self):
        #initialize and start the game
        self.current_card = 0
        self.next_card = 0
        self.guess = ""
        self.is_playing = True
        self.score = 0
        self.total_score = 300 #we start the game at 300
        #initialize the variables we will use

        self.current_card = Card()
        self.next_card = Card()
        #assign classes to the current and next cards using card.py

    def start_game(self):

        while self.is_playing:
            #we will call the functions here that the director goes through
            self.get_cards()
            self.show_current_card()
            self.get_guess()
            self.find_score()
            self.do_outputs()

    def get_cards(self):
        if not self.is_playing:
            return

        #assigns values to the current_card and the next_card using the draw() function on card.py

    def show_current_card(self):
        if not self.is_playing:
            return

        #print the current card for the user to see


    def get_guess(self):
        if not self.is_playing:
            return

        #get the guess of h or l from the user


    def find_score(self):
        if not self.is_playing:
            return
            
        #give the user score if they were correct or not

        #add the user score, negative or positive, to the total score

    def do_outputs(self):
        if not self.is_playing:
            return

        #print the next card value

        #print the total score

        #get user input if they want to play again y or n