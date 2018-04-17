#!/usr/bin/env python3
# SSH transport class based on PT-security lectures
import paramiko

def get_transport(transport_name, host, port, login, password):
    pass

class SSHtransport():
    def __init__(self, host = 'localhost', port = 22022, login = 'root', password = 'pwd'):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
        self.client.connect(hostname = host, username = login, password = password, port = port)

    def __del__(self):
        self.client.close()

    def exec(self, command = 'ls -a'):
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.read()

    def get_file(self, file_name = 'file', remote_path = './', local_path = './'):
        file_remote = remote_path + file_name
        file_local = local_path + file_name
        sftp = self.client.open_sftp()
        sftp.get(file_remote, file_local)
        sftp.close()
        
def main():
    base_client = SSHtransport()
    print( base_client.exec('uname -a') )
    base_client.get_file('getme')

if __name__ == "__main__":
    main()