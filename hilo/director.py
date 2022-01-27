from hilo.card import Card


class Director:
    '''Attributes: current_card(int), next_card(int), is_playing(boolean), score(int), total_score(int)'''

    def __init__(self):
        '''Constructs new Director
        Arg: self'''

        # initialize and start the game
        self.current_card = Card()
        self.next_card = Card()
        self.guess = ""
        self.is_playing = True
        self.score = 0
        self.total_score = 300  # we start the game at 300
        # initialize the variables we will use

    def start_game(self):
        '''Starts the game by running the main game loop.
        Arg: self'''

        while self.is_playing:
            # we will call the functions here that the director goes through
            self.get_cards()
            self.show_current_card()
            self.get_guess()
            self.find_score()
            self.outputs()
            self.play_again()

    def get_cards(self):
        if not self.is_playing:
            return
        card = Card()
        card.draw()
        print(card.current_card)
        # assigns values to the current_card and the next_card using the draw() function on card.py

    def show_current_card(self):
        if not self.is_playing:
            return

        # print the current card for the user to see

    def get_guess(self):
        '''Determines if user guesses higher or lower.
        Arg: self'''
        if not self.is_playing:
            return

        # get the guess of h or l from the user
        self.guess = input("Higher or lower? [h/l] ")

    def find_score(self):
        '''Determines user's score according to guess input.
        Arg: self'''
        if not self.is_playing:
            return

        # give the user score if they were correct or not
        # add the user score, negative or positive, to the total score
        if self.current_card < self.next_card and self.guess == 'h':
            self.score += 100

        elif self.current_card > self.next_card and self.guess == 'l':
            self.score += 100

        elif self.current_card < self.next_card and self.guess == 'l':
            self.score -= 75

        elif self.current_card > self.next_card and self.guess == 'h':
            self.score -= 75

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

    def outputs(self):
        '''Show outputs for user.
        Arg: self'''
        if not self.is_playing:
            return

        # print the next card value and total score
        print(f"The card is: {}")
        print(f"Next card was: {}")
        print(f"Your score is: {self.total_score}")
        self.is_playing == (self.score > 0)

    def play_again(self):
        '''Determines if user wants to play again.
        Arg: self'''
        play = input("Play again? [y/n] ")
        self.is_playing = (play == "y")
