#!/usr/bin/env python3
# Create database
import json
import sqlite3
import os.path

_json_db = None
_db_name = 'configs/controls.json'
db = sqlite3.connect('database.db')

def get_full_path():
    my_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(my_path, _db_name)

def get_db():
    global _json_db
    if not _json_db:
        with open(get_full_path(),'r') as f:
            _json_db = json.load(f)
    return _json_db

def create_db():
    curr = db.cursor()
    curr.execute('''CREATE TABLE if not exists
        control(id INTEGER PRIMARY KEY, descr TEXT)''')
    curr.execute('''CREATE TABLE if not exists
        scandata(id INTEGER PRIMARY KEY, descr TEXT, status TEXT)''')
    controls = get_db()
    for string in controls:
        curr.execute("INSERT INTO control(id, descr) VALUES(?, ?)", (string[0], string[1]))
    db.commit()
    db.close()

def add_control(control_id, status):
    pass

create_db()