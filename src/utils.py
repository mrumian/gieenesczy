import uuid
from requests import codes as CODE
import logging as log


def generate_uuid():
    generated_uuid = uuid.uuid4()
    log.debug('Generated UUID: %s' % generated_uuid)
    return generated_uuid


def post_json(session, core_address, path, data, expected_status_code=200):
    log.debug('Post action\n'
              'Address: %s\n'
              'Data: %s' % (core_address + path, data))

    response = session.post(core_address + path, json=data)

    if response.status_code == expected_status_code:
        log.debug('Post success')
        log.debug('Response content: %s' % response.json())
        return True
    else:
        log.error('Post action encountered problems\n'
                  'Status code: %d\n'
                  'Message: %s' % (response.status_code, response.json()))
        return False


def get(session, core_addres, path):
    log.debug('Get action\n'
              'Address: %s' % core_addres + path)

    response = session.get(core_addres + path)

    if response.status_code == CODE.ok:
        log.debug('Get success')
        log.debug('Response content: %s' % response.json())
        return True
    else:
        log.error('Get action encountered problems\n'
                  'Status code: %d\n'
                  'Message: %s' % (response.status_code, response.json()))
        return False
