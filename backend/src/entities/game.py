from .board import Board
from .player import Player

# Game class. Where all game logic will be implemented
class Game:

    board = Board()
    someoneWon = False

    # by omission, the opponent will be the CPU
    def __init__(self, player1, token1, player2 = 'CO'):
        token2 = 'O' if token1 == 'X' else 'X'
        self.player1 = Player(player1, token1)
        self.player2 = Player(player2, token2)

    def player2Play(self):
        print('player 2')

    def player1Play(self):
        print('player 1')

    # select between each player alternatly
    def nextPlay(self, i):
        self.player1Play() if i % 2 == 0 else self.player2Play()

    # main procedure
    def beginGame(self):
        i = 0
        while not self.someoneWon:
            self.board.printBoard()
            self.nextPlay(i)
            #checkForWin(i)
            i += 1
            


        print(self.player1.name, self.player1.token, self.player2.name, self.player2.token)