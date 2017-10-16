from marshmallow_enum import EnumField

from src.structures.schema import Schema
from src.enums.enums import DataLinkType as DTLEnum


class DataLinkType(Schema):
    Ethernet = EnumField(DTLEnum)
