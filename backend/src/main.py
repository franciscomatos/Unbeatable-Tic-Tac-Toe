from .entities.board import Board, BoardSchema
from .entities.player import Player, PlayerSchema
from .entities.game import Game

from flask import Flask, jsonify, request 
from flask_cors import CORS 

# creating the Flask application

app = Flask(__name__)
CORS(app) # We need Cross-Origin Resource Sharing

# playerName = input('Enter your name: ')
# playerToken = int(input('Select token: 1 - X, 2 - O: '))

# while playerToken not in [1, 2]:
#     print('Something went wrong')
#     playerToken = input('Select token: 1 - X, 2 - O: ')
#     print(playerToken)

playerName = 'Francisco'
playerToken = 1

token = 'X' if playerToken == 1 else 'O'
game = Game(playerName, token)
# game.beginGame()

@app.route('/test')
def get_player1():
    schema = PlayerSchema(many=False)
    player = schema.dump(game.player1)
    return jsonify(player.data)
