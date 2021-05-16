import random


# TODO: Define the Dealer class here.
class Dealer:

    """ (AH):
    The responsibility of this class of objects is to ...
    deal a card before and after user guesses higher or lower;
    Then calculate the score based on whether the guess was correct.

    Attributes:
        card (integer): a random card drawn with value between 1 to 13.
    """

    def __init__(self):
        """

        The constructor declares and initializes instance attributes
        with their default values.

        (AH) The class constructor.
        Args:  self (Dealer) : an instance of Dealer.
        """

    def deal_cards(self):
        """ (MireyaL To Do.)

        The deal_cards method randomly generates a card value between 1 to 13.

        Rule 1: Individual cards are represented as a number from 1 to 13.
        Rule 3: The director displays the current card.
        Rule 5: The director shows the next card.

        Args:

        """
        self.card = random.randint(1, 13)
        return self.card

    def get_points(self, guess, current_card, next_card):
        """
        (SarahA To Do.)

        The get_points method calculates and returns the points from each guess.
        Rule 6: The dealer earns 100 points if they guessed correctly.
        Rule 7: The dealer loses 75 points if they guessed incorrectly.

        Args:
        guess (list of two elements): Either h for higher or l for lower.
        """

        # (AH)
        if guess.lower() == "h" and next_card > current_card:
            points = 100
        elif guess.lower() == "l" and next_card < current_card:
            points = 100
        else:
            points = -75

        # (AH) points will be added to the total score in Director class.
        return points

