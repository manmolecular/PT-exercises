#!/usr/bin/env python3
# SSH transport class based on PT-security lectures
import paramiko

default_host = 'localhost'
default_port = 22022
default_login = 'root'
default_password = 'pwd'

# Class for error handling
class TransportError(Exception):
    def __init__(self, message = 'unknown error'):
        self.full_message = 'TransportError: ' + message
        print(self.full_message)

# SSH transport class
class SSHtransport():
    def __init__(self, host = default_host, port = default_port, login = default_login, password = default_password):
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
            self.client.connect(hostname = host, username = login, password = password, port = port)
        except:
            TransportError('can not connect to host')
            
    def __del__(self):
        self.client.close()

    def exec(self, command = ''):
        if not command:
            raise TransportError('argument *command* is empty')
        else:
            stdin, stdout, stderr = self.client.exec_command(command)
            return stdout.read()

    def get_file(self, file_name = '', remote_path = './', local_path = './'):
        if not file_name:
            raise TransportError('argument *file_name* is empty')
        else:
            file_remote = remote_path + file_name
            file_local = local_path + file_name
            sftp = self.client.open_sftp()
            sftp.get(file_remote, file_local)
            sftp.close()

# Get unique transport of some class
def get_transport(transport_name, host = default_host, port = default_port, login = default_login, password = default_password):
    try:
        return transport_name(host, port, login, password);
    except:
        TransportError('Unknown transport')
        
def main():
    base_client = get_transport(SSHtransport)
    print( base_client.exec('ls') )
    base_client.get_file('getme')

if __name__ == "__main__":
    main()