#!/usr/bin/env python3
# Main module for scripts calling
from transports import *
from get_db import *
import os
import importlib

_scriptdir = 'scripts'

# Import all scripts from folder
def import_scripts():
    for file in os.listdir('./' + _scriptdir):
            if file.endswith('.py') and file != '__init__.py':
                importlib.import_module(_scriptdir + '.' + file[:-3])

def main():
    import_scripts()

if __name__ == "__main__":
    main()