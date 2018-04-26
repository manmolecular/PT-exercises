#!/usr/bin/env python3
# First test - check file existense
from get_db import *
from transports import *
import os.path

_database = 'database.db'
_file_name = 'testfile'
_status = None
_control_id = 0

try:
    SSHtransport = get_transport('SSH')
except:
    _status = 4
try:
    SSHtransport.get_file(_file_name)
    _status = 1
except:
    _status = 2

def main():
    if not os.path.isfile('./' + _database):
        create_db()
    add_control(_control_id, _status)