from game.dealer import Dealer
from random import randint
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
        self.dealer = Dealer()
        self.card = 0

    def clear_screen(self):
        """
        Checks for OS type, then sends command to clear terminal.

        Args:
            self (Director): an instance of Director.
        """
        os.system('cls' if os.name == 'nt' else 'clear')


    def start_game(self):
        """
        Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """
        self.clear_screen()
        self.display_intro()

        while self.keep_playing:
            self.clear_screen()
            self.draw_card()
            
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
        self.card = randint(1,13)

    def get_points(self):
        """
        Updates the score of the game after each round
        
        Args:
            self (Director): An instance of Director.
        """
        hl = nextCard-lastCard
        if((hl>=0 and guess == 'h') or (hl<= 0 and guess == 'l')):
            self.score += 100
        else:
            self.score += -75

    def print_cards(self):


    # def run_game(self):
    #     """ (MireyaL To Do.)

    #     Outputs the important game information for each round of play.
    #     In this case, it means the cards drawn, guess higher/lower, and the score.

    #     Args:
    #         self (Director): An instance of Director.
    #     """

    #     print()
    #     # TODO: print current_card

    #     # Rule 4: The dealer guesses if the next one will be higher or lower.
    #     # (AH) use string method .lower() to ensure comparison == will be ok.
    #     # TODO: guess = # need a lowercase h or l from user input.

    #     # TODO: print next_card

    #     # (AH) Call method update_points(guess) to get class attribute of score.
    #     # TODO: print score

	# # TODO: insert code from W04 Solo Checkpoint Dice program.
    #     print()
