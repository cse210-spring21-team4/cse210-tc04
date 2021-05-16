
class Dealer:
    """A code template for a dealer. Can ask the player to guess the next card
    and can ask player if they want to continue playing.

    Attributes:
        is_it_higher: Returns boolean of whether player guessed the card was higher.
        wants_to_continue: Returns boolean of whether player wants to keep playing.
    """

    def __init__(self):
        """initialize instance attributes.

        Args:
            self (Dealer): An instance of Dealer.
        """

    def is_it_higher(self):
        """
        Returns boolean of whether player guessed the card was higher.
        Args:
            self (Director): An instance of Director.
        """
        return True if input('Higher or lower? [h/l] ').lower() == 'h' else False

    def want_to_continue(self):
        """
        Returns boolean of whether player wants to keep playing.
        Args:
            self (Director): An instance of Director.
        """
        return True if input('Keep playing? [y/n] ').lower() == 'y' else False    