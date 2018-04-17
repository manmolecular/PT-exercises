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

    def exec(self, command = 'uname -a'):
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.read()

    def get_file(self, path):
        # work on it
        pass

def main():
    base_client = SSHtransport()
    print(base_client.exec())

if __name__ == "__main__":
    main()