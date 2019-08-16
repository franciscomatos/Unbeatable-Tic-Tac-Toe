from marshmallow import Schema, fields

# Move class. Will contain the position and the points
class Move:

    def __init__(self, position, points = 0):
        self.position = position
        self.points = points

    def setPoints(self, points):
        self.points = points

    def __eq__(self, other):
        return self.points == other

    def __lt__(self, other):
        return self.points < other

    def __gt__(self, other):
        return self.points > other

# serializable class
class Move(Schema):
    position = fields.Number()
    points = fields.Number()
    player = fields.String()