import uuid
import logging as log


def generate_uuid():
    generated_uuid = uuid.uuid4()
    log.debug('Generated UUID: %s' % generated_uuid)
    return generated_uuid


def post(session, core_address, path, data, expected_status_code):
    log.debug('Post action\n'
              'Address: %s\n'
              'Data: %s' % (core_address + path, data))

    response = session.post(core_address + path, json=data)

    if response.status_code == expected_status_code:
        log.debug('Post success')
        log.debug('Response content: %s' % response.json())
        return response.text
    else:
        log.error('Post action encountered problems\n'
                  'Status code: %d\n'
                  'Message: %s' % (response.status_code, response.json()))
        return response.text


def get(session, core_addres, path, expected_status_code):
    log.debug('Get action\n'
              'Address: %s' % core_addres + path)

    response = session.get(core_addres + path)

    if response.status_code == expected_status_code:
        log.debug('Get success')
        log.debug('Response content: %s' % response.json())
        return True
    else:
        log.error('Get action encountered problems\n'
                  'Status code: %d\n'
                  'Message: %s' % (response.status_code, response.json()))
        return False


def delete(session, core_address, path, expected_status_code):
    log.debug('Delete action\n'
              'Address: %s' % core_address + path)

    response = session.delete(core_address + path)

    if response.status_code == expected_status_code:
        log.debug('Delete success')
        log.debug('Response content: %s' % response.json())
        return True
    else:
        log.error('Delete action encountered problems\n'
                  'Status code: %d\n'
                  'Message: %s' % (response.status_code, response.json()))


def put(session, core_address, path, data, expected_status_code):
    log.debug('Put action\n'
              'Address: %s\n'
              'Data: %s' % (core_address + path, data))

    response = session.put(core_address + path, data)

    if response.status_code == expected_status_code:
        log.debug('Put success')
        log.debug('Response content: %s' % response.json())
        return True
    else:
        log.error('Put action encountered problems\n'
                  'Status code: %d\n'
                  'Message: %s' % (response.status_code, response.json()))
