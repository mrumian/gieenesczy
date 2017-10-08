from marshmallow import Schema, fields
from marshmallow_enum import EnumField
import logging as log

from src.enums import project_status


# http://gns3-server.readthedocs.io/en/latest/api/v2/controller/project.html

class Project:
    def __init__(self, **kwargs):
        self.schema = ProjectSchema()
        self.data = kwargs
        self.json = self._to_json()

    def _to_json(self):
        json, error = self.schema.dump(self.data)

        if error:
            raise ValueError('Error occurred during deserialization: %s' % error)
        else:
            return json


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
