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


    def delete_link(self, link_uuid):
        log.debug('Deleting link')

        delete(self.session, self.address, '/projects/%s/links/%s' %(proj_uuid, link_uuid))
