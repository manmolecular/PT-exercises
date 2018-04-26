#!/usr/bin/env python3
# Create database
import json
import sqlite3
import os.path

_json_db = None
_db_contest = 'configs/controls.json'
_db_name = 'database.db'

statuses = {
        1: 'STATUS_COMPLIANT',
        2: 'STATUS_NOT_COMPLIANT',
        3: 'STATUS_NOT_APPLICABLE',
        4: 'STATUS_ERROR',
        5: 'STATUS_EXCEPTION'
    }

def get_db():
    return sqlite3.connect(_db_name)

def get_full_path():
    my_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(my_path, _db_contest)

def get_db():
    global _json_db
    if not _json_db:
        with open(get_full_path(),'r') as f:
            _json_db = json.load(f)
    return _json_db

def create_db():
    db = get_db()
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
    db = get_db()
    curr = db.cursor()
    descr = str(curr.execute("SELECT descr FROM control WHERE id = ?", 
        str(control_id)).fetchone())[2:-3]

    if not curr.execute("SELECT id FROM scandata WHERE id = ?", str(control_id)).fetchone():
        curr.execute("INSERT INTO scandata(id, descr, status) VALUES(?, ?, ?)", 
            (control_id, descr, statuses[status]))

    db.commit()
    db.close()