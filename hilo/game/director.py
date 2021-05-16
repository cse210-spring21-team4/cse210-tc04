from dealer import Dealer
from random import sample
import os
class Director:
    """A code template for a person who directs the game. This class keeps
    track of the score and controls the sequence of play.

    Attributes:
        display_intro: Prints introductory information and rules to the console.
        keep_playing (boolean): Whether or not the dealer wants to keep playing.
        score (number): The total number of points earned.
        dealer (Dealer): An instance of the class of objects known as Dealer.
        card (integer): Random integer between 1 to 13.
    """

    def __init__(self):
        """
        The class constructor.

        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.score = 300
        self.deck = [range(1, 14)]
        self.card = 0
        self.dealer = Dealer()

    def clear_screen(self):
        """
        Checks for OS type, then sends command to clear terminal.

        Args:
            self (Director): an instance of Director.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def play_game(self):
        """
        Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """
        self.clear_screen()
        self.display_intro()

        self.draw_card()
        while self.keep_playing:
            self.clear_screen()
            print(f'The card is: {self.card}')
            self.previous = self.card
            self.draw_card()
            self.get_points()
            print(f'Your score is: {self.score}')
            if not self.dealer.want_to_continue():
                break
            
    def display_intro(self):
        """
        Prints introductory information and rules to the console.

        Args:
            self (Director): an instance of Director.
        """
        
        print("\nThis game is Hi-Lo.")
        print(f"Your starting score is {self.score}.\n")
        print("You gain 100 points if you guess correctly,")
        print("but you lose 75 points if you guess incorrectly.")
        print("When your score is 0, this game is over.\n\n")
        input("Press enter to begin.")

    def can_play(self):
        """
        Verifies that game can still be played.
        Args:
            self (Director): An instance of Director.
        """
        self.keep_playing = (self.score > 0)

    def draw_card(self):
        """ 
        Determine cards for each round of play.

        Args:
            self (Director): An instance of Director.
        """
        
        # If the deck is depleted (i.e. the list is empty), 'reshuffle' it.
        if not self.deck:
             self.deck = list(range(1,14))

        # Pick a card, any card.
        self.card = sample(self.deck, 1)

        # 'Remove' (delete) the card from the 'deck' (list)
        self.deck.remove(self.card)

    def get_points(self):
        """
        Updates the score of the game.
        
        Args:
            self (Director): An instance of Director.
        """
        if(self.card > self.previous) == self.dealer.is_it_higher():
            self.score += 100
        else:
            self.score += -75