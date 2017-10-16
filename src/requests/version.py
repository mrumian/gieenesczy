from requests import codes as CODE

from src.requests.session import Session
from src.request_utils import *


class Version(Session):
    def __init__(self):
        super().__init__()
        self.session = Session().session
        self.address = Session().address

    def get_version(self):
        get(self.session, self.address, '/version', CODE.ok)
