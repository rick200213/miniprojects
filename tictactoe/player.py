import math
import random
class Player:
    def __init__(self,letter):
        #letter is x or o
        self.letter=letter

        #we want all players toget their next move given a game
        def get_name(self,game):
            pass
class  RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        square = random.choice(game.avialable_moves())
        return square
class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    def get_move(self,game):
        valid_square ='False'
        val = None
        while not valid_square:
            square= input(self.letter + '\'s turn. Input move (0,9):')
            #we're going to check that this is a correct value by trying to cast
            #it can be type cast an integer, if the value entered is a number else the input is invalid
            #if that spot is not available on the board, we have to declare that it is an invalid input
            try:
                val = int(square)
                if val not in game.avialable_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val
