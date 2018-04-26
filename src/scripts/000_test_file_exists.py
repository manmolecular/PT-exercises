#!/usr/bin/env python3
# First test - check file existense
from db_handling import *
from transports import *
import os.path

_database = 'database.db'
_file_name = 'te1stfile'
_status = None
_control_id = 0

_status = 1
try:
    get_transport('SSH').get_file(_file_name)
except TransportUnknown:
    _status = 4
except TransportIOError:
     _status = 2

def main():
    if not os.path.isfile('./' + _database):
        create_db()
    add_control(_control_id, _status)