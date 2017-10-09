from marshmallow import fields
from marshmallow_enum import EnumField

from src.enums import project_status
from .schema import Schema


# http://gns3-server.readthedocs.io/en/latest/api/v2/controller/project.html

class Project:
    def __init__(self, **kwargs):
        self.schema = ProjectSchema(strict=True)
        self.data = kwargs
        self.json = self._to_json()

    def _to_json(self):
        self.schema.validate(self.data)

        return self.schema.dump(self.data).data


class ProjectSchema(Schema):
    auto_close = fields.Bool()
    auto_open = fields.Bool()
    auto_start = fields.Bool()
    filename = fields.Str()
    name = fields.Str()
    path = fields.Str()
    project_id = fields.UUID()
    scene_height = fields.Int()
    scene_width = fields.Int()
    status = EnumField(project_status)
