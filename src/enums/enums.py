from enum import Enum


class ProjectStatus(Enum):
    opened = 'opened'
    closed = 'closed'


class DataLinkType(Enum):
    DLT_ATM_RFC1483 = 'DLT_ATM_RFC1483'
    DLT_EN10MB = 'DLT_EN10MB'
    DLT_FRELAY = 'DLT_FRELAY'
    DLT_C_HDLC = 'DLT_C_HDLC'
    DLT_PPP_SERIAL = 'DLT_PPP_SERIAL'


class LinkType(Enum):
    ETHERNET = 'ethernet'
    SERIAL = 'serial'


class NodeType(Enum):
    cloud = 'cloud'
    nat = 'nat'
    ethernet_hub = 'ethernet_hub'
    ethernet_switch = 'ethernet_switch'
    frame_relay_switch = 'frame_relay_switch'
    atm_switch = 'atm_switch'
    docker = 'docker'
    dynamips = 'dynamips'
    vpcs = 'vpcs'
    virtualbox = 'virtualbox'
    vmware = 'vmware'
    iou = 'iou'
    qemu = 'qemu'


class NodeStatus(Enum):
    stopped = 'stopped'
    started = 'started'
    suspended = 'suspended'


class ConsoleType(Enum):
    vnc = 'vnc'
    telnet = 'telnet'
    http = 'http'
    null = 'null'
