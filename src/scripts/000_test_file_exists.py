#!/usr/bin/env python3
# First test - check file existense
from get_db import *
from transports import *

_file_name = 'testfile'
_status = None

try:
    SSHtransport = get_transport('SSH')
except:
    _status = 4
try:
    SSHtransport.get_file(_file_name)
    _status = 1
except:
    _status = 2

create_db()
add_control(000, _status)