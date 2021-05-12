def can_play(points): 
    #checks if the player has any points left.
    return (points <= 0)
        


def get_points(guess, nextCard, lastCard):
    #checks if the guess was right and returns the coorisponding points.
    hl = nextcard-lastCard
    if((hl>=0 and guess == 'h') or (hl<= 0 and guess == 'l')):
        return 100
    else:
        return -75