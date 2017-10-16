from marshmallow import fields

from src.structures.schema import Schema


class NodeProperties(Schema):
    startup_script = fields.Str()
