from requests import codes as CODE

from src.requests.session import Session
from src.request_utils import *

from src.log import log_action


class Compute(Session):
    compute_data = None
    compute_list = None

    def __init__(self, session):
        super().__init__()
        self.session = session.session
        self.address = session.address

    def register_compute_server(self, data):
        log_action('Register Compute Server')

        link = '/computes'

        self.compute_data = post(self.session, self.address, link, data, CODE.created)

    def get_compute_server_data(self):
        log_action('Get Compute Server Data')

        link = '/computes'

        self.compute_list = get(self.session, self.address, link, CODE.ok)


    #########
    # Helpers
    #########

    def get_compute_id_for_name(self, name):
        return [compute['compute_id'] for compute in self.compute_list if compute['name'] == name][0]
