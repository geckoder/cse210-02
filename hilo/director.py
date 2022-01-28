from card import Card


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
        '''Assigns values to the current_card and the next_card using the draw() function '''
        if not self.is_playing:
            return

        self.current_card.draw()  # already assigned in Card()
        self.next_card.draw()

    def show_current_card(self):
        '''Prints the current card for the user to see'''
        if not self.is_playing:
            return

        # current_card is an integer so we need to call random_card
        # if is a string would be self.current_card
        print(f"The card is: {self.current_card.random_card}")

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
            self.score = 100

        elif self.current_card > self.next_card and self.guess == 'l':
            self.score = 100

        elif self.current_card < self.next_card and self.guess == 'l':
            self.score = -75

        elif self.current_card > self.next_card and self.guess == 'h':
            self.score = -75

        self.total_score += self.score

    def outputs(self):
        '''Show outputs for user.
        Arg: self'''
        if not self.is_playing:
            return

        # print the next card value and total score
        print(f"Next card was: {self.next_card.random_card}")  # like on lines
        print(f"Your score is: {self.total_score}")
        self.is_playing == (self.score > 0)

    def play_again(self):
        '''Determines if user wants to play again.
        Arg: self'''
        play = input("Play again? [y/n] ")
        self.is_playing = (play == "y")
