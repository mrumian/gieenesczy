from requests import codes as CODE

from .session import Session
from src.request_utils import *

# http://gns3-server.readthedocs.io/en/latest/api/v2/controller/link.html


class Link(Session):
    def __init__(self):
        super().__init__()
        self.session = Session().session
        self.address = Session().address
        self.link = Link()

    def create_link(self, project_uuid, data):
        log.debug('Creating link')

        expected_status_code = CODE.created
        link = '/projects/%s/links' % project_uuid

        post(self.session, self.address, link, data, expected_status_code)

    def get_link(self, project_uuid, link_uuid):
        log.debug('Get link: %s' % link_uuid)

        expected_status_code = CODE.ok
        link = '/projects/%s/links/%s' % (project_uuid, link_uuid)

        get(self.session, self.address, link, expected_status_code)

    def get_all_links(self, project_uuid):
        log.debug('Get links from project: %s' % project_uuid)

        expected_status_code = CODE.ok
        link = '/projects/%s/links' % project_uuid

        get(self.session, self.address, link, expected_status_code)

    def delete_link(self, project_uuid, link_uuid):
        log.debug('Delete link: %s' % link_uuid)

        expected_status_code = CODE.no_content
        link = '/projects/%s/links/%s' % (project_uuid, link_uuid)

        delete(self.session, self.address, link, expected_status_code)

    def update_link(self, project_uuid, link_uuid, data):
        expected_status_code = CODE.created
        link = '/projects/%s/links/%s' % (project_uuid, link_uuid)
        log.debug('Update link: %s' % link_uuid)

        put(self.session, self.address, link, data, expected_status_code)

    def start_capture(self, project_uuid, link_uuid):
        expected_status_code = CODE.created
        link = '/projects/%s/links/%s/start_capture' % (project_uuid, link_uuid)
        log.debug('Start capture for link: %s' % link_uuid)

        post(self.session, self.address, link, None, expected_status_code)

    def stop_capture(self, project_uuid, link_uuid):
        expected_status_code = CODE.created
        link = '/projects/%s/links/%s/stop_capture' % (project_uuid, link_uuid)
        log.debug('Stop capture for link: %s' % link_uuid)

        post(self.session, self.address, link, None, expected_status_code)

    def stream_pcap(self, project_uuid, link_uuid):
        expected_status_code = CODE.ok
        link = '/projects/%s/links/%s/pcap' % (project_uuid, link_uuid)
        log.debug('Stream PCAP for link: %s' % link_uuid)

        get(self.session, self.address, link, expected_status_code)
