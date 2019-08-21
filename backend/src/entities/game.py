from .board import Board
from .player import Player
from .move import Move

import random
import copy

# Game class. Where all game logic will be implemented
class Game:

    board = Board()
    availablePositions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    nextMove = 0

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
                del self.availablePositions[i]
                break

    # finds the row and column correspondent to the index and calls board insertion method
    # also updates the available positions list  
    def insertSymbol(self, position, token):
        print('gonna insert ', token, ' in ', position)
        for i in range(3):
            for j in range(3):
                print('board position: ', self.board.board[i][j], ' position: ')
                if self.board.board[i][j] == position:
                    self.board.insertPosition(i, j, token)
                    self.foundFreePosition = True
                    self.removeFromAvailable(position)

    # finds the row and column correspondent to the index and calls specific board insertion method
    def insertSymbolSpecificBoard(self, board, position, token):
        for i in range(3):
            for j in range(3):
                if board.board[i][j] == position: board.board[i][j] = token 
                    
    # method to be called in every iteration of the minimax algorithm to find every possible move
    def findAvailablePositions(self, board):
        availableMoves = []
        # available moves for the next play
        for row in board.board:
            for position in row:
                if position != self.player1.token and position != self.player2.token:
                    availableMoves.append(position)

        return availableMoves

    # method to select the highest score in the list of available moves
    def minimize(self, availableMoves):
        minimum = availableMoves[0]
        for move in availableMoves[1:]:
            if move < minimum: minimum = move

        self.nextMove = minimum.position
        
        return minimum

    # method to select the highest score in the list of available moves
    def maximize(self, availableMoves):
        maximum = availableMoves[0]
        for move in availableMoves[1:]:
            if move > maximum: maximum = move

        self.nextMove = maximum.position

        return maximum

    # minimax algorithm implementation
    def findBestMove(self, board, currentToken, nextToken):
        # depending on the token we will have to maximize or to minimize

        # list of all available positions
        availablePositions = self.findAvailablePositions(board)

        # check for terminal states
        winner = self.checkWin(board, availablePositions)
        if winner == 0: return 0 #tie
        elif winner == 1 and currentToken == self.player1.token: return 10 # it was supposed to be player 1 turn, which means the AI won
        elif winner == 1 and currentToken == self.player2.token: return -10 # it was supposed to be AI turn, which means the player 1 won

        availableMoves = []
        newBoard = Board(copy.deepcopy(board.board)) # we make a new board, which will be altered to contain the new possible move
        for index in availablePositions:
            self.insertSymbolSpecificBoard(newBoard, index, currentToken)
            nextMove = Move(index, self.findBestMove(newBoard, nextToken, currentToken)) # recursion happens here
            availableMoves.append(nextMove) # new move is created for each empty position, score is 0 by default
            newBoard = Board(copy.deepcopy(board.board))

        # now that all moves have been used, time to choose the best one (max or min)
        # player 1 turn, must choose the min
        if currentToken == self.player1.token: return self.minimize(availableMoves)
        else: return self.maximize(availableMoves)
        
    # player 2 (CPU) logic
    def player2Play(self):
        print(self.player2.name + "'s turn")
        # first time it's called with the original board and the AI token

        self.findBestMove(Board(copy.deepcopy(self.board.board)), self.player2.token, self.player1.token)
        self.insertSymbol(self.nextMove, self.player2.token)

        # in case something goes wrong
        if not self.foundFreePosition:
            print('Invalid position!')
            self.player2Play()

        self.foundFreePosition = False

    # player 1 logic
    def player1Play(self):
        print(self.player1.name + "'s turn")

        try:
            position = input('Select one of the available positions: ')
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
    def checkWinRightDiagonal(self, board):
        diagonal = []
        for i, j in zip(range(3), range(2, -1, -1)):
            diagonal.append(board.getPosition(i,j))

        return diagonal[1:] == diagonal[:-1]

    # check for winner left diagonals
    def checkWinLeftDiagonal(self, board):
        diagonal = []
        for i in range(3):
            diagonal.append(board.getPosition(i,i))
        return diagonal[1:] == diagonal[:-1]

    # check for winner diagonals
    def checkWinDiagonal(self, board):
        if self.checkWinLeftDiagonal(board): return True
        if self.checkWinRightDiagonal(board): return True

        return False

    # check for winner columns
    def checkWinVertical(self, board):
        flag = False
        column = []
        for i in range(3):
            for j in range(3):
                column.append(board.getPosition(j,i))
            if column[1:] == column[:-1]:
                flag = True
                break
            column = []

        return flag

    # check for winner rows
    def checkWinHorizontal(self, board):
        flag = False
        for row in board.board:
            if row[1:] == row[:-1]:
                flag = True
                break

        return flag

    # check for a win horizontaly, verticaly and diagonaly
    def checkWin(self, board, availablePositions):
        if self.checkWinHorizontal(board): return 1
        elif self.checkWinVertical(board): return 1
        elif self.checkWinDiagonal(board): return 1
        elif len(availablePositions) == 0: return 0
        
        return 2

    # main procedure
    def beginGame(self):
        i = 0
        winner = 0 # flag for game end and for winner
        while True:
            self.board.printBoard()
            self.nextPlay(i)
            winner = self.checkWin(self.board, self.availablePositions)
            if winner != 2 : break
            i += 1
            
        self.board.printBoard()

        if winner == 0:
            print("it's a tie")
        elif winner == 1 and i % 2 == 0:
            print('winner is ', self.player1.name)
        else:
            print('winner is ', self.player2.name)
