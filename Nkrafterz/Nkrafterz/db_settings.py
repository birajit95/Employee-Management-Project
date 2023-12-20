import sqlite3


def get_connection():
    connection = sqlite3.connect('db.sqlite3')
    return connection