#!/usr/bin/env python3
# Main module
from transports import *

def main():
    base_client = get_transport('SSH')
    base_client.exec('ls -a')
    print(base_client.exec('ls -a'))
    #base_client.get_file('getme')

if __name__ == "__main__":
    main()