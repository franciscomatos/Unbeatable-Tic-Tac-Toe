# Board class. Used to represent the board and associated methods
class Board:

    # board itself
    # not sure about list of list, probably will change it to a single list
    board = [[1,2,3], [4,5,6], [7,8,9]]

    def __init__(self):
        pass

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
            