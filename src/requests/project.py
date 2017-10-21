from requests import codes as CODE

from .session import Session
from src.request_utils import *

from src.log import log_action


class Project(Session):
    project_data = None
    projects_list = None

    def __init__(self, session):
        super().__init__()
        self.session = session.session
        self.address = session.address

    # http://gns3-server.readthedocs.io/en/latest/api/v2/controller/project/projects.html
    def create_project(self, data):
        log_action('Create project')

        expected_status_code = CODE.created
        link = '/projects'

        self.project_data = post(self.session, self.address, link, data, expected_status_code)

    def get_all_projects(self):
        log_action('Get all projects')

        expected_status_code = CODE.ok
        link = '/projects'

        self.projects_list = get(self.session, self.address, link, expected_status_code)

    # http://gns3-server.readthedocs.io/en/latest/api/v2/controller/project/projectsprojectid.html#v2-projects-project-id
    def get_project(self, project_uuid):
        log_action('Get project:' % project_uuid)

        expected_status_code = CODE.ok
        link = '/projects/%s' % project_uuid

        self.project_data = post(self.session, self.address, link, expected_status_code)

    # http://gns3-server.readthedocs.io/en/latest/api/v2/controller/project/projectsload.html
    def load_project(self, path, **kwargs):
        log_action('Load project: %s' % path)

        expected_status_code = CODE.created
        link = '/projects/load'
        data = {
            'path': path
        }

        data.update(kwargs)

        self.project_data = post(self.session, self.address, link, data, expected_status_code)

    # http://gns3-server.readthedocs.io/en/latest/api/v2/controller/project/projectsprojectid.html#put-v2-projects-project-id
    def update_project(self, project_uuid, data):
        log_action('Update project: %s' % project_uuid)

        expected_status_code = CODE.ok
        link = '/projects/%s' % project_uuid

        self.project_data = put(self.session, self.address, link, data, expected_status_code)

    # http://gns3-server.readthedocs.io/en/latest/api/v2/controller/project/projectsprojectid.html#delete-v2-projects-project-id
    def delete_project(self, project_uuid):
        log_action('Delete project: %s' % project_uuid)

        expected_status_code = CODE.no_content
        link = '/projects/%s' % project_uuid

        delete(self.session, self.address, link, expected_status_code)

    #########
    # Helpers
    #########

    def get_key(self, key):
        return self.project_data[key]

    def get_project_uuid(self):
        return self.project_data['project_id']

    def get_project_path(self):
        return self.project_data['path']

    def get_project_name(self):
        return self.project_data['name']

    def get_project_filename(self):
        return self.project_data['filename']
