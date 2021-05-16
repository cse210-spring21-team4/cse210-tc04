from game.dealer import Dealer


class Director:
    """A code template for a person who directs the game.
    The responsibility of this class of objects is to keep track
    of the score and control the sequence of play.

    Attributes:
        keep_playing (boolean): Whether or not the dealer wants to keep playing.
        score (number): The total number of points earned.
        dealer (Dealer): An instance of the class of objects known as Dealer.
        current_card (integer): Random integer between 1 to 13.
        next_card (integer): Random integer between 1 to 13.
    """

    def __init__(self):
        """ (AgnesH To Do.)

        The class constructor.

        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.dealer = Dealer()

        # Rule 2: The dealer starts the game with 300 points.
        self.score = 300
        # Rule 3: The director displays the current card.
        self.current_card = Dealer()
        # Rule 4: The dealer guesses if the next one will be higher or lower.
        # Note: guess does not need to be a Class Attribute.
        # guess = ["h", "l"]
        # Rule 5: The director shows the next card.
        self.next_card = Dealer()

    def start_game(self):
        """ (AgnesH To Do.)

        Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """

        # (AH) Introduce Hi-Lo game.
        print()
        print("This game is Hi-Lo.")
        print(f"Your starting score is:  {self.score}")
        print("You gain 100 points if you guess correctly,")
        print("but you lose 75 points if you guess incorrectly.")
        print("When your score is 0, this game is over.")

        while self.keep_playing:
            self.get_cards()
            self.run_game()
            # moved call for update_points(self, guess) into run_game().

    def get_cards(self):
        """ (DaltonW To Do.)

        Gets the inputs at the beginning of each round of play.
        In this case, that means:
        Rule 3: The director displays the current card.
        Rule 5: The director shows the next card.

        Args:
            self (Director): An instance of Director.
        """
        self.current_card = self.dealer.deal_cards()
        self.next_card = self.dealer.deal_cards()

    def update_points(self, guess, current_card, next_card):
        """ (KeltonG To Do.)

        Updates the important game information for each round of play.
        In this case, that means updating the score.

        Args:
            self (Director): An instance of Director.
        """
        points = self.dealer.get_points(guess, current_card, next_card)
        self.score += points

    def can_play(self):
        """
        (SarahA To Do.)

        (AH) The can_play method determines whether or not the Dealer
            can continue playing. It returns a boolean value
            that is true if the score > 0.
            Otherwise, it returns false.
        """
        if self.score > 0:
            return True
        else:
            return False

    def run_game(self):
        """ (MireyaL To Do.)

        Outputs the important game information for each round of play.
        In this case, it means the cards drawn, guess higher/lower, and the score.

        Args:
            self (Director): An instance of Director.
        """

        print()
        print(f"The card is:  {self.current_card}")

        # Rule 4: The dealer guesses if the next one will be higher or lower.
        # (AH) use string method .lower() to ensure comparison == will be ok.
        guess = input("Higher or lower? [h/l]:  ").lower()

        print(f"Next card was:  {self.next_card}")

        # (AH) Call method update_points(guess) to get class attribute of score.
        self.update_points(guess, self.current_card, self.next_card)
        print(f"Your score is: {self.score}")

        if self.can_play():
            choice = input("Keep playing? [y/n] ")
            self.keep_playing = choice == "y"
        else:
            self.keep_playing = False
        print()
