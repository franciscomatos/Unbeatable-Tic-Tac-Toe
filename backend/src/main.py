from .entities.board import Board
from .entities.player import Player
from .entities.game import Game

playerName = input('Enter your name: ')
playerToken = int(input('Select token: 1 - X, 2 - O: '))

while playerToken not in [1, 2]:
    print('Something went wrong')
    playerToken = input('Select token: 1 - X, 2 - O: ')
    print(playerToken)

game = Game(playerName, playerToken)
game.beginGame()