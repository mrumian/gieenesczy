from marshmallow import fields
from marshmallow_enum import EnumField

from src.enums.enums import Protocol
from src.structures.schema import Schema
from src.structures.sub_structers.capabilities import Capabilities


class Compute:
    def __init__(self, **kwargs):
        self.schema = ComputeSchema(strict=True)
        self.data = kwargs
        self.json = self._to_json()

    def _to_json(self):
        self.schema.validate(self.data)

        return self.schema.dump(self.data).data


class ComputeSchema(Schema):
    capabilities = fields.Nested(Capabilities)
    compute_id = fields.Str()
    connected = fields.Bool()
    cpu_usage_percent = fields.Number()
    host = fields.Str()
    memory_usage_percent = fields.Number()
    name = fields.Str()
    port = fields.Int()
    protocol = EnumField(Protocol, by_value=True)
    user = fields.Str()
