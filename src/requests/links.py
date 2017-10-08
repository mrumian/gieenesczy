from .session import Session
from src.utils import *
import logging as log
from requests import codes as CODE
from .projects import Project


class Links(Session):
    def __init__(self):
        super().__init__()
        self.session = Session().session
        self.address = Session().address
        self.link = Links()
        self.project = Project()

    def create_link(self):
        log.debug('Creating link')

        res = self.link.loads(post_json(self.session, self.address, '/projects/%s/links' % self.project., data, expected_status_code=CODE.created))

        print(res.data)


    def load_project(self, path, **kwargs):
        log.debug('Loading project from: %s' % path)

        data = {
            'path': path
        }
        data.update(kwargs)

        post_json(self.session, self.address, '/projects/load', data, expected_status_code=CODE.created)
