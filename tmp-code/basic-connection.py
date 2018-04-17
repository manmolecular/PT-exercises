#!/usr/bin/env python3
# Basic SSH connection with paramiko
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.load_host_keys(filename='./known_hosts')
client.connect(hostname='localhost', username='root', password='pwd', port=22022)
stdin, stdout, stderr = client.exec_command('apt list --installed')
results = stdout.read()
print(results[:100])
client.close()