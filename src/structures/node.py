from marshmallow import fields
from marshmallow_enum import EnumField

from .schema import Schema
from src.enums.enums import NodeStatus, NodeType, ConsoleType
from src.structures.sub_structers.label import Label
from src.structures.sub_structers.port import Port
from src.structures.sub_structers.node_properties import NodeProperties


class Node:
    def __init__(self, **kwargs):
        self.schema = NodeSchema(strict=True)
        self.data = kwargs
        self.json = self._to_json()

    def _to_json(self):
        self.schema.validate(self.data)

        return self.schema.dump(self.data).data


class NodeSchema(Schema):
    command_line = fields.Str()
    compute_id = fields.Str()
    console = fields.Int()
    console_host = fields.Str()
    console_type = EnumField(ConsoleType)
    first_port_name = fields.Str()
    height = fields.Int()
    label = fields.Nested(Label)
    name = fields.Str()
    node_directory = fields.Str()
    node_id = fields.UUID()
    node_type = EnumField(NodeType)
    port_name_format = fields.Str()
    port_segment_size = fields.Str()
    ports = fields.Nested(Port, many=True)
    project_id = fields.UUID()
    properties = fields.Nested(NodeProperties)
    status = EnumField(NodeStatus)
    symbol = fields.Str()
    width = fields.Int()
    x = fields.Int()
    y = fields.Int()
    z = fields.Int()
