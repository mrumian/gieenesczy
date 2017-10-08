from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from src.enums import project_status


# http://gns3-server.readthedocs.io/en/latest/api/v2/controller/project.html

class Project(Schema):
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
