from marshmallow import fields
from marshmallow_enum import EnumField

from src.structures.schema import Schema
from src.enums.enums import NodeType


class Capabilities(Schema):
    version = fields.Str()
    platform = fields.Str()
    Ethernet = fields.Nested(EnumField(NodeType, by_value=True), many=True)
