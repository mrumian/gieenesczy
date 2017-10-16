from marshmallow import fields
from marshmallow_enum import EnumField

from src.structures.schema import Schema
from src.structures.sub_structers.data_link_type import DataLinkType
from src.enums.enums import LinkType


class Port(Schema):
    adapter_number = fields.Int()
    data_link_types = fields.Nested(DataLinkType)
    link_type = EnumField(LinkType)
    name = fields.Str()
    port_number = fields.Int()
    short_name = fields.Str()
