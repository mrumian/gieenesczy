from enum import Enum


class DataLinkType(Enum):
    DLT_ATM_RFC1483 = 'DLT_ATM_RFC1483'
    DLT_EN10MB = 'DLT_EN10MB'
    DLT_FRELAY = 'DLT_FRELAY'
    DLT_C_HDLC = 'DLT_C_HDLC'
    DLT_PPP_SERIAL = 'DLT_PPP_SERIAL'
