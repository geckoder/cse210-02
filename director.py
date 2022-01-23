from cards import Card


class Director:
    '''Attributes: card(list[Card]), is_playing(boolean), score(int)'''

    def __init__(self):
        '''Constructs new Director
        Arg: self'''
        self.card = []
        self.is_playing = True
        self.score = 0

        for i in range(5):
            draw = Card()
            self.card.append(draw)

    def start_game(self):
        '''Starts the game by running the main game loop.
        Arg: self'''

        while self.is_playing:
            self.guess_card
            self.do_updates()
            self.do_outputs()
            self.play_again()

    def guess_card(self):
        '''Determines if user guesses higher or lower.
        Arg: self'''
        guess_card = input("Higher or lower? [h/l] ")
        # TO DO: determine is guess was right

    def play_again(self):
        '''Determines if user wants to play again.
        Arg: self'''
        draw_card = input("Play again? [y/n] ")
        self.is_playing = (draw_card == "y")

    def do_updates(self):
        '''Updates user's score.
        Arg: self'''
        pass

    def do_outputs(self):
        '''Show outputs for user.
        Arg: self'''

        print(f"The card is: {self.cards_num}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)
