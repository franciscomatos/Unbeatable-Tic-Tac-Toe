from marshmallow import Schema, fields

# class Player. Used to maintain player information
class Player:

    def __init__(self, name, token):
        self.name = name
        self.token = token

# serializable class
class PlayerSchema(Schema):
    name = fields.Str()
    token = fields.Str()