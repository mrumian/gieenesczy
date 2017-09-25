import requests


class Session:

    def __init__(self, protocol='http', server_name='localhost', port=3080, version='v2', user='admin',
                 password='admin'):
        self.server_name = server_name
        self.port = port
        self.protocol = protocol
        self.version = version
        self.address = '%s://%s:%d/%s' % (self.protocol, self.server_name, self.port, self.version)
        self.auth = (user, password)
        self.session = self._create_session()

    def _create_session(self):
        session = requests.session()
        session.auth = self.auth
        return session
