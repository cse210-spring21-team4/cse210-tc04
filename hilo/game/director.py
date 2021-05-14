from game.dealer import dealer

class Director:

    def do_updates(self):
        """Updates the score of the game after each round

        Args:
            self (Director): An instance of Director.
        """
        points = self.dealer.get_points()
        self.score += points