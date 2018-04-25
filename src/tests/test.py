#!/usr/bin/env python3
# Tests for SSH transport class based on PT-security lectures
from transports import *
import pytest

def test_get_transport_exc():
    get_transport('SSH', 'localhost', '22022', 'root', 'pwd')
    get_transport('SSH')
    with pytest.raises(UnknownTransport):
        get_transport('', 'localhost', '22022', 'root', 'pwd')

def test_init_exc():
    SSHtransport('localhost', '22022', 'root', 'pwd')
    with pytest.raises(TransportConnectionError):
        SSHtransport('_unknownhost_', '22022', 'root', 'pwd')
        SSHtransport('localhost', '_unknownport_', 'root', 'pwd')
        SSHtransport('localhot', '22022', '_unknownuser_', 'pwd')
        SSHtransport('localhot', '22022', 'root', '_unknownpass_')

def test_exec_exc():
    SSHtransport('localhost', '22022', 'root', 'pwd').exec('ls')
    with pytest.raises(TransportError):
        SSHtransport('localhost', '22022', 'root', 'pwd').exec('')

def test_get_file_name_exc():
    SSHtransport('localhost', '22022', 'root', 'pwd').get_file('getme')
    with pytest.raises(TransportError):
        SSHtransport('localhost', '22022', 'root', 'pwd').get_file('')

def test_get_file_remote_exc():
    with pytest.raises(TransportError):
        SSHtransport('localhost', '22022', 'root', 'pwd').get_file('_unknownfile_')