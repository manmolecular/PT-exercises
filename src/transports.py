#!/usr/bin/env python3
# SSH transport class based on PT-security lectures
import paramiko
import socket
import json

with open('config.json', 'r') as f:
    file_config = json.load(f)

defaults = {
        'host': file_config['host'], 
        'port':file_config['transports']['SSH']['port'], 
        'login':file_config['transports']['SSH']['login'], 
        'password':file_config['transports']['SSH']['password']
    }
transport_names = ['SSHtransport']

# Classes for error handling
class UnknownTransport(Exception):
    def __init__(self, error_args):
        Exception.__init__(self, 'UnknownTransport {}'.format(error_args))
        self.error_args = error_args

class TransportError(Exception):
    def __init__(self, error_args):
        Exception.__init__(self, 'TransportError {}'.format(error_args))
        self.error_args = error_args

class TransportConnectionError(Exception):
    def __init__(self, error_args):
        Exception.__init__(self, 'TransportConnectionError {}'.format(error_args))
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

    def get_file(self, file_name = '', remote_path = './', local_path = './'):
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

# Get unique transport of some class
def get_transport(transport_name, host, port, login, password):
    if transport_name not in transport_names:
        raise UnknownTransport({'transport_name':transport_name})
    return globals()[transport_name](host, port, login, password)

def main():
    pass
    # base_client = get_transport('SSHtransport', 'localhost', '22022', 'root', 'pwd')
    # base_client.exec('ls -a')
    # base_client.get_file('getme')

if __name__ == "__main__":
    main()