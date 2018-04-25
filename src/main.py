#!/usr/bin/env python3
# Main module
from transports import *
import os
import importlib

_scriptdir = 'scripts'

def import_scripts():
    for file in os.listdir('./' + _scriptdir):
            if file.endswith('.py') and file != '__init__.py':
                importlib.import_module(_scriptdir + '.' + file[:-3])

def main():
    import_scripts()

    base_client = get_transport('S1SH')
    base_client.exec('ls -a')
    print(base_client.exec('ls -a'))
    #base_client.get_file('getme')

if __name__ == "__main__":
    main()