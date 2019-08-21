from marshmallow import Schema, fields

# Board class. Used to represent the board and associated methods
class Board:

    def __init__(self, board = [['1','2','3'], ['4','5','6'], ['7','8','9']]):
        # board itself
        self.board = board

    # modifies the board
    def insertPosition(self, line, column, token):
        self.board[line][column] = token

    # access board position
    def getPosition(self, line, column):
        return self.board[line][column]

    # prints the board in the tic tac toe format
    def printBoard(self):
        for row in self.board:
            print('|', end='')
            for index in row:
                print(index, end='|')
            print()
            

# serializable class
class BoardSchema(Schema):
    board = fields.List(fields.List(fields.Str()), required=True)

# serializable class
class WinSchema(Schema):
    win = fields.Boolean()

# serializable class
#class BoardSchema(Schema):
#    board = fields.List(fields.Number(), required=True)