#!/usr/bin/env python3
# SSH transport class based on PT-security lectures
from get_config import *

import paramiko
import socket
import json

# Some helpful dicts for using
_get_file_defaults = {
        'file_name': 'testfile',
        'remote_path': './',
        'local_path': './'
    }
_transport_names = {
        'SSH':'SSHtransport'
    }

# Classes for error handling
class TransportError(Exception):
    def __init__(self, error_args):
        Exception.__init__(self, 'TransportError {}'.format(error_args))
        self.error_args = error_args

class UnknownTransport(TransportError):
    def __init__(self, error_args):
        TransportError.__init__(self, error_args)
        self.error_args = error_args

class TransportConnectionError(TransportError):
    def __init__(self, error_args):
        TransportError.__init__(self, error_args)
        self.error_args = error_args

# SSH transport class
class SSHtransport():
    def __init__(self, host, port, login, password):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.client.connect(hostname = host, username = login, password = password, port = port)
        except  paramiko.BadHostKeyException:
            raise TransportConnectionError('paramiko: BadHostKeyException')
        except  paramiko.AuthenticationException:
            raise TransportConnectionError('paramiko: AuthenticationException')
        except paramiko.SSHException:
            raise TransportConnectionError('paramiko: SSHException')
        except socket.error:
            raise TransportConnectionError('paramiko: socket.error')
        except:
            raise TransportConnectionError('connection refused by unknown reason')
            
    def __del__(self):
        self.client.close()

    def exec(self, command = ''):
        if not command:
            raise TransportError({'command':command})
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.read()

    def get_file(self, file_name = _get_file_defaults['file_name'], 
        remote_path = _get_file_defaults['remote_path'], local_path = _get_file_defaults['local_path']):
        if not file_name:
            raise TransportError({'file_name':file_name})
        file_remote = remote_path + file_name
        file_local = local_path + file_name
        sftp = self.client.open_sftp()
        try:
            sftp.stat(file_remote)
        except:
            raise TransportError('file doesnt exist')
        sftp.get(file_remote, file_local)
        sftp.close()

# Get defaults from config file
def get_defaults(transport_name):
    _json_config = get_config()
    return {
        'host': _json_config['host'], 
        'port':_json_config['transports'][transport_name]['port'], 
        'login':_json_config['transports'][transport_name]['login'], 
        'password':_json_config['transports'][transport_name]['password']
    }

# Get unique transport of some class
def get_transport(transport_name, host = '', port = '', login = '', password = ''):
    if transport_name not in _transport_names:
        raise UnknownTransport({'transport_name':transport_name})
    
    default = get_defaults(transport_name)
    if not host:
        host = default['host']
    if not port:
        port = default['port']
    if not login:
        login = default['login']
    if not password:
        password = default['password']

    return globals()[_transport_names[transport_name]](host, port, login, password)