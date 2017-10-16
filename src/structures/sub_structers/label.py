from marshmallow import fields

from src.structures.schema import Schema


class Label(Schema):
    rotation = fields.Int()
    style = fields.Str()
    text = fields.Str()
    x = fields.Int()
    y = fields.Int()
