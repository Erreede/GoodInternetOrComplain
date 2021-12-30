import sqlite3
import json
import datetime
from sqlite3 import Error

def createConnection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect('db/GoodInternetOrComplain.db')
        checkTable(conn)
        return conn
    except Error as e:
        print(e)

def checkTable(conn):
    """ create a main table to store results if it does't exist """
    try:
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS speedResults (id integer PRIMARY KEY, timestamp integer NOT NULL, data text NOT NULL);')
    except Error as e:
        print(e)

def insertResults(conn, data):
    """ store results """
    try:
        c = conn.cursor()
        c.execute('INSERT INTO speedResults (timestamp, data) VALUES (?, ?);', (datetime.datetime.utcnow().timestamp(), json.dumps(data)))
        conn.commit()
    except Error as e:
        print(e)