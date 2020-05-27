import sqlite3 as db
from datetime import datetime


def init():
    """
    Creating table if it doesn't exist
    """
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


def log(amount, category, message=""):
    """
    Inserting record into database based on amount, category,
    and message passed
    """
    date = str(datetime.now())
    connect = db.connect("spent.db")
    cursor = connect.cursor()
    SQL = '''
    INSERT INTO EXPENSES VALUES (
         {},
        '{}',
        '{}',
        '{}'
    )
    '''.format(amount, category, message, date)
    cursor.execute(SQL)
    connect.commit()


def delete(amount, category, message=""):
    """
    Deleting record based on amount, category, and message
    passed in
    """
    connect = db.connect("spent.db")
    cursor = connect.cursor()
    if message and len(message) > 0:
        SQL = '''
        DELETE FROM EXPENSES WHERE Amount = {} AND Category = '{}' AND Message = '{}'
        '''.format(amount, category, message)
    else:
        SQL = '''
        DELETE FROM EXPENSES WHERE Amount = {} AND Category = '{}'
        '''.format(amount, category, message)
    try:
        cursor.execute(SQL)
        connect.commit()
    except:
        print("Please enter all fields. Try again!")


def view(category=None):
    """
    Looking at entries in database
    """
    connect = db.connect("spent.db")
    cursor = connect.cursor()
    if category:
        SQL = '''
        SELECT * FROM EXPENSES WHERE Category = '{}'
        '''.format(category)
        SQLtotal = '''
        SELECT SUM(Amount) FROM EXPENSES WHERE Category = '{}'
        '''.format(category)
    else:
        SQL = '''
        SELECT * FROM EXPENSES
        '''
        SQLtotal = '''
        SELECT SUM(Amount) FROM EXPENSES
        '''.format(category)
    cursor.execute(SQL)
    results = cursor.fetchall()
    cursor.execute(SQLtotal)
    totalAmount = cursor.fetchone()[0]

    return totalAmount, results
