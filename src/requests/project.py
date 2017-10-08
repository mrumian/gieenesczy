from requests import codes as CODE

from .session import Session
from src.utils import *


class Project(Session):
    def __init__(self):
        super().__init__()
        self.session = Session().session
        self.address = Session().address
        self.project = Project()

    # http://gns3-server.readthedocs.io/en/latest/api/v2/controller/project/projects.html
    def create_project(self, data):
        log.debug('Create project')

        expected_status_code = CODE.created
        link = '/projects'

        post(self.session, self.address, link, data, expected_status_code)

    def get_all_projects(self):
        log.debug('Get all projects')

        expected_status_code = CODE.ok
        link = '/projects'

        get(self.session, self.address, link, expected_status_code)

    # http://gns3-server.readthedocs.io/en/latest/api/v2/controller/project/projectsprojectid.html#v2-projects-project-id
    def get_project(self, project_uuid):
        log.debug('Get project:' % project_uuid)

        expected_status_code = CODE.ok
        link = '/projects/%s' % project_uuid

        post(self.session, self.address, link, expected_status_code)

    # http://gns3-server.readthedocs.io/en/latest/api/v2/controller/project/projectsload.html
    def load_project(self, path, **kwargs):
        log.debug('Load project: %s' % path)

        expected_status_code = CODE.created
        link = '/projects/load'
        data = {
            'path': path
        }

        data.update(kwargs)

        post(self.session, self.address, link, data, expected_status_code)

    # http://gns3-server.readthedocs.io/en/latest/api/v2/controller/project/projectsprojectid.html#put-v2-projects-project-id
    def update_project(self, project_uuid, data):
        log.debug('Update project: %s' % project_uuid)

        expected_status_code = CODE.ok
        link = '/projects/%s' % project_uuid

        put(self.session, self.address, link, data, expected_status_code)

    # http://gns3-server.readthedocs.io/en/latest/api/v2/controller/project/projectsprojectid.html#delete-v2-projects-project-id
    def delete_project(self, project_uuid):
        log.debug('Delete project: %s' % project_uuid)

        expected_status_code = CODE.no_content
        link = '/projects/%s' % project_uuid

        delete(self.session, self.address, link, expected_status_code)
