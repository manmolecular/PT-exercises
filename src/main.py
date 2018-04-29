#!/usr/bin/env python3
# Main module for scripts calling
from transports import *
from db_handling import *
import os
import importlib

_database = 'database.db'
_scriptdir = 'scripts'

# Import all scripts from folder
def import_scripts():
    for file in os.listdir('./' + _scriptdir):
            if file.endswith('.py') and file != '__init__.py':
                status = importlib.import_module(_scriptdir + '.' + file[:-3]).main()
                script_id = int(file[0:3])
                add_control(script_id, status)

def main():
    if not os.path.isfile('./' + _database):
        create_db()
    import_scripts()

if __name__ == "__main__":
    main()