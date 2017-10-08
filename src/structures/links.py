from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from src.enums import link_type


# http://gns3-server.readthedocs.io/en/latest/api/v2/controller/link/projectsprojectidlinks.html


class Links(Schema):
    capture_file_name = fields.Str()
    capture_file_path = fields.Str()
    capturing = fields.Bool()
    link_id = fields.UUID
    link_type = EnumField(link_type)
    nodes = [fields.Nested(Node)]
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
