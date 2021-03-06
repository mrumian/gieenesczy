from marshmallow import fields
from marshmallow_enum import EnumField

from src.enums.enums import LinkType
from src.enums.enums import DataLinkType
from .schema import Schema

# http://gns3-server.readthedocs.io/en/latest/api/v2/controller/link.html


class Link(Schema):
    capture_file_name = fields.Str()
    capture_file_path = fields.Str()
    data_link_type = EnumField(DataLinkType)
    capturing = fields.Bool()
    link_id = fields.UUID
    link_type = EnumField(LinkType)
    nodes = fields.Nested(Node, many=True)
    project_id = fields.UUID


class Node(Schema):
    adapter_number = fields.Int()
    label = fields.Nested(Label)
    node_id = fields.UUID
    port_number = fields.Int()


class Label(Schema):
    rotation = fields.Int()
    style = fields.Str()
    text = fields.Str()
    x = fields.Int()
    y = fields.Int()
