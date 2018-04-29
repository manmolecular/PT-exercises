#!/usr/bin/env python3
# First test - check file existense
from db_handling import *
from transports import *

_file_name = 'testfile'

def main():
    try:
        get_transport('SSH').get_file(_file_name)
    except TransportUnknown:
        return 4
    except TransportIOError:
        return 2
    return 1