from .session import Session
from src.utils import *
import logging as log
from requests import codes as CODE


class Projects(Session):
    def __init__(self):
        super().__init__()
        self.session = Session().session
        self.address = Session().address

    def create_project(self, name, **kwargs):
        log.debug('Creating project: %s' % name)

        data = {
            'name': name
        }
        data.update(kwargs)

        post_json(self.session, self.address, '/projects', data, expected_status_code=CODE.created)
