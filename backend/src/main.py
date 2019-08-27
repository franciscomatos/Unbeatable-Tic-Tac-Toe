from .entities.board import Board, BoardSchema
from .entities.player import Player, PlayerSchema
from .entities.game import Game
from .entities.move import Move, MoveSchema

from flask import Flask, jsonify, request 
from flask_cors import CORS 

playerName = 'Francisco'
playerToken = 1
token = 'X' if playerToken == 1 else 'O'


class Main:

    def __init__(self):
        self.game = Game(playerName, token)

    def runApp(self):
        # creating the Flask application
        self.app = Flask(__name__)
        CORS(self.app) # We need Cross-Origin Resource Sharing
# playerName = input('Enter your name: ')
# playerToken = int(input('Select token: 1 - X, 2 - O: '))

# while playerToken not in [1, 2]:
#     print('Something went wrong')
#     playerToken = input('Select token: 1 - X, 2 - O: ')
#     print(playerToken)


# game.beginGame()

#@app.route('/test')
#def get_player1():
#    schema = PlayerSchema(many=False)
#    player = schema.dump(game.player1)
#    return jsonify(player.data)


main = Main()
# creating the Flask application
app = Flask(__name__)
CORS(app) # We need Cross-Origin Resource Sharing

@app.route('/reset')
def resetGame():
    del main.game
    main.game = Game(playerName, token)
    print('game board: ', main.game.board.board)
    return getBoard()

@app.route('/board')
def getBoard():
    schema = BoardSchema(many=False)
    board = schema.dump(main.game.board)
    print(board.data)
    return jsonify(board.data)

@app.route('/board/win')
def checkWin():
    winner = False if main.game.checkWin(main.game.board, main.game.availablePositions) == 2 else True
    return jsonify(winner)

@app.route('/move/player', methods = ['POST'])
def postMove():
    print('gonna insert')
    # mount new move
    posted_move = MoveSchema()\
        .load(request.get_json())

    move = Move(**posted_move.data)

    print("move position: ", move.position)

    main.game.insertSymbol(str(int(move.position)), main.game.player1.token)
    main.game.foundFreePosition = False
    return getBoard()
    # return created exam
    #new_move = MoveSchema().dump(move).data
    #return jsonify(new_move), 201

@app.route('/move/opponent')
def opponentMove():
    print('opponent move')
    main.game.player2Play()
    return getBoard()