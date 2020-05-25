import sqlite3 as db


def init():
    connect = db.connect("spent.db")
    cursor = connect.cursor()
    SQL = '''
    CREATE TABLE IF NOT EXISTS EXPENSES (
        Amount number,
        Category string,
        Message string,
        Date string
    )
    '''
    cursor.execute(SQL)
    connect.commit()


init()
