from marshmallow import Schema as MarshmallowSchema


class Schema(MarshmallowSchema):

    def validate(self, data, *args, **kwargs):
        if set(data.keys()) - set(self.fields.keys()):
            raise AttributeError(set(data.keys()) - set(self.fields.keys()))
        super(Schema, self).validate(data, *args, **kwargs)
