import logging as log

log.basicConfig(level=log.DEBUG)


def log_action(action_text='', ch='=', length=90):
    log.debug(('%s{:%s^%d}%s' % (ch, ch, length, ch)).format(action_text))
