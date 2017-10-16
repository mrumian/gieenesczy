from requests import codes as CODE

from src.requests.session import Session
from src.request_utils import *


class Node(Session):
    node_data = None
    nodes_list = None

    def __init__(self, session):
        self.session = session.session
        self.address = session.address

    def create_node(self, data):
        log.debug('Create node')

        link = '/projects/%s/nodes' % data['project_id']

        self.node_data = post(self.session, self.address, link, data, CODE.created)
