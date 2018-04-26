#!/usr/bin/env python3
# Tests for SSH transport class based on PT-security lectures
from transports import *
import pytest

SSHdefaults = get_defaults('SSH')

def test_SSH_get_transport_exc():
    get_transport('SSH', SSHdefaults['host'], SSHdefaults['port'], 
        SSHdefaults['login'], SSHdefaults['password'])
    get_transport('SSH')
    with pytest.raises(UnknownTransport):
        get_transport('', SSHdefaults['host'], SSHdefaults['port'], 
            SSHdefaults['login'], SSHdefaults['password'])

def test_SSH_init_exc():
    SSHtransport(SSHdefaults['host'], SSHdefaults['port'], 
        SSHdefaults['login'], SSHdefaults['password'])
    with pytest.raises(TransportConnectionError):
        SSHtransport('_unknownhost_', SSHdefaults['port'], 
            SSHdefaults['login'], SSHdefaults['password'])
        SSHtransport(SSHdefaults['host'], '_unknownport_', 
            SSHdefaults['login'], SSHdefaults['password'])
        SSHtransport(SSHdefaults['host'], SSHdefaults['port'], 
            '_unknownlogin_', SSHdefaults['password'])
        SSHtransport(SSHdefaults['host'], '_unknownport_', 
            SSHdefaults['login'], '_unknownpass_')

def test_SSH_exec_exc():
    SSHtransport(SSHdefaults['host'], SSHdefaults['port'], 
        SSHdefaults['login'], SSHdefaults['password']).exec('ls')
    with pytest.raises(TransportError):
        SSHtransport(SSHdefaults['host'], SSHdefaults['port'], 
            SSHdefaults['login'], SSHdefaults['password']).exec('')

def test_SSH_get_file_name_exc():
    SSHtransport(SSHdefaults['host'], SSHdefaults['port'], 
        SSHdefaults['login'], SSHdefaults['password']).get_file('testfile')
    with pytest.raises(TransportError):
        SSHtransport(SSHdefaults['host'], SSHdefaults['port'], 
            SSHdefaults['login'], SSHdefaults['password']).get_file('')

def test_SSH_get_file_remote_exc():
    with pytest.raises(TransportError):
       SSHtransport(SSHdefaults['host'], SSHdefaults['port'], 
            SSHdefaults['login'], SSHdefaults['password']).get_file('_unknownfile_')