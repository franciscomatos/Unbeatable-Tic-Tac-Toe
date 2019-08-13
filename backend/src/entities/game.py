from .board import Board
from .player import Player
import random

# Game class. Where all game logic will be implemented
class Game:

    board = Board()
    availablePositions = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    someoneWon = False
    foundFreePosition = False

    # by omission, the opponent will be the CPU
    def __init__(self, player1, token1, player2 = 'CO'):
        token2 = 'O' if token1 == 'X' else 'X'
        self.player1 = Player(player1, token1)
        self.player2 = Player(player2, token2)

    # available positions list update
    def removeFromAvailable(self, position):
        for i in range(len(self.availablePositions)):
            if self.availablePositions[i] == position:
                print('gonna remove ', i)
                del self.availablePositions[i]
                break

    # finds the row and column correspondent to the index and calls board insertion method
    # also updates the available positions list  
    def insertSymbol(self, position, token):
        for i in range(3):
            for j in range(3):
                if self.board.board[i][j] == position:
                    self.board.insertPosition(i, j, token)
                    self.foundFreePosition = True
                    self.removeFromAvailable(position)

    # minimax algorithm implementation
    # for now just a random
    def findBestMove(self):
        return random.choice(self.availablePositions)

    # player 2 (CPU) logic
    def player2Play(self):
        print(self.player2.name + "'s turn")
        position = self.findBestMove()
        
        self.insertSymbol(position, self.player2.token)

        # in case something goes wrong
        if not self.foundFreePosition:
            print('Invalid position!')
            self.player2Play()

        self.foundFreePosition = False

    # player 1 logic
    def player1Play(self):
        print(self.player1.name + "'s turn")

        try:
            position = int(input('Select one of the available positions: '))
            self.insertSymbol(position, self.player1.token)
        except ValueError:
            print('Invalid Position')
            self.player1Play()
            return

        # in case something goes wrong
        if not self.foundFreePosition:
            print('Invalid position!')
            self.player1Play()
            return 

        self.foundFreePosition = False

    # select between each player alternatly
    def nextPlay(self, i):
        self.player1Play() if i % 2 == 0 else self.player2Play()

    # check for winner left diagonals
    def checkWinRightDiagonal(self):
        diagonal = []
        for i, j in zip(range(3), range(2, -1, -1)):
            diagonal.append(self.board.getPosition(i,j))

        print(diagonal[1:], diagonal[:-1], diagonal[1:] == diagonal[:-1])
        return diagonal[1:] == diagonal[:-1]

    # check for winner left diagonals
    def checkWinLeftDiagonal(self):
        diagonal = []
        for i in range(3):
            diagonal.append(self.board.getPosition(i,i))
        print(diagonal[1:], diagonal[:-1], diagonal[1:] == diagonal[:-1])
        return diagonal[1:] == diagonal[:-1]

    # check for winner diagonals
    def checkWinDiagonal(self):
        if self.checkWinLeftDiagonal(): return True
        if self.checkWinRightDiagonal(): return True

        return False

    # check for winner columns
    def checkWinVertical(self):
        flag = False
        column = []
        for i in range(3):
            for j in range(3):
                column.append(self.board.getPosition(j,i))
            if column[1:] == column[:-1]:
                flag = True
                break
            column = []

        return flag

    # check for winner rows
    def checkWinHorizontal(self):
        flag = False
        for row in self.board.board:
            if row[1:] == row[:-1]:
                flag = True
                break

        return flag

    # check for a win horizontaly, verticaly and diagonaly
    def checkWin(self):
        print(len(self.availablePositions))
        if len(self.availablePositions) == 0: return True
        elif self.checkWinHorizontal(): return True
        elif self.checkWinVertical(): return True
        elif self.checkWinDiagonal(): return True
        
        return False

    # main procedure
    def beginGame(self):
        i = 0
        while True:
            self.board.printBoard()
            self.nextPlay(i)
            if self.checkWin(): break
            i += 1
            
        self.board.printBoard()
        print('Winner is: ', self.player1.name if i%2 ==0 else self.player2.name)