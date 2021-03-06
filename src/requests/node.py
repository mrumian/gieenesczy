from requests import codes as CODE

from src.requests.session import Session
from src.request_utils import *

from src.log import log_action


class Node(Session):
    node_data = None
    nodes_list = None

    def __init__(self, session, project_id):
        super().__init__()
        self.session = session.session
        self.address = session.address
        self.project_id = project_id

    def create_node(self, data):
        log_action('Create node')

        link = '/projects/%s/nodes' % self.project_id

        self.node_data = post(self.session, self.address, link, data, CODE.created)
