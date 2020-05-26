import sqlite3 as db
from datetime import datetime


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


def log(amount, category, message=""):
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
    connect = db.connect("spent.db")
    cursor = connect.cursor()
    SQL = '''
    DELETE FROM EXPENSES WHERE Amount = {} AND Category = '{}' AND MESSAGE = '{}'
    '''
    try:
        cursor.exequte(SQL)
    except:
        print("Please enter all fields. Try again!")
    connect.commit()


def view(category=None):
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
        SELECT SUM(Amount) FROM EXPENSES WHERE Category = '{}'
        '''.format(category)
    cursor.execute(SQL)
    results = cursor.fetchall()
    cursor.execute(SQLtotal)
    totalAmount = cursor.fetchone()[0]

    return totalAmount, results


print(view('gas'))
