from marshmallow import Schema, fields


# http://gns3-server.readthedocs.io/en/latest/api/v2/controller/project/projects.html#post-v2-projects

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
    status = fields.Str()
