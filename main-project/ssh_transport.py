#!/usr/bin/env python3
# SSH transport class based on PT-security lectures
import paramiko
import traceback

defaults = {'host': 'localhost', 'port':22022, 'login':'root', 'password':'pwd'}
transport_names = ['SSHtransport']

# Classes for error handling
class UnknownTransport(Exception):
    def __init__(self, error_args):
        print(error_args)
        Exception.__init__(self, 'UnknownTransport {}'.format(error_args))
        self.error_args = error_args

class TransportError(Exception):
    def __init__(self, error_args):
        print(error_args)
        Exception.__init__(self, 'TransportError {}'.format(error_args))
        self.error_args = error_args

class TransportConnectionError(Exception):
    def __init__(self, error_args):
        print(error_args)
        Exception.__init__(self, 'TransportConnectionError {}'.format(error_args))
        self.error_args = error_args

# SSH transport class
class SSHtransport():
    def __init__(self, host, port, login, password):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
        try:
            self.client.connect(hostname = host, username = login, password = password, port = port)
        except:
            raise TransportConnectionError('{connection refused}')
            
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
            raise TransportError('{file doesnt exist}')
        sftp.get(file_remote, file_local)
        sftp.close()

# Get unique transport of some class
def get_transport(transport_name, host, port, login, password):
    if transport_name not in transport_names:
        raise UnknownTransport({'transport_name':transport_name})
    return globals()[transport_name](host, port, login, password)

def main():
    base_client = get_transport('SSHtransport', 'localhost', '22022', 'root', 'pwd')
    print( base_client.exec('ls -a') )
    base_client.get_file('get2me')

if __name__ == "__main__":
    main()