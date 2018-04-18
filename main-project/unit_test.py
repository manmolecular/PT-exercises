#!/usr/bin/env python3
# Tests for SSH transport class based on PT-security lectures
from ssh_transport import *
import pytest

def test_get_transport_exc():
    with pytest.raises(UnknownTransport):
        get_transport('', 'localhost', '22022', 'root', 'pwd')

def test_init_exc():
    with pytest.raises(TransportConnectionError):
        SSHtransport('localhot', '22022', 'root', 'pwd')

def test_exec_exc():
    with pytest.raises(TransportError):
        SSHtransport('localhost', '22022', 'root', 'pwd').exec('')

def test_get_file_name_exc():
    with pytest.raises(TransportError):
        SSHtransport('localhost', '22022', 'root', 'pwd').get_file('')

def test_get_file_remote_exc():
    with pytest.raises(TransportError):
        SSHtransport('localhost', '22022', 'root', 'pwd').get_file('_unknownfile_')