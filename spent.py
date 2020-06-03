import sqlite3 as db
from datetime import datetime


def init(totalIncome):
    """
    Creating table if it doesn't exist
    """
    connect = db.connect("test.db")
    cursor = connect.cursor()
    ExpensesTable = '''
    CREATE TABLE IF NOT EXISTS Expenses (
        Amount number,
        Category string,
        Message string,
        Date string
    )
    '''

    IncomeTable = '''
    CREATE TABLE IF NOT EXISTS Income (
        payAmount number,
        payCategory string,
        payMessage string,
        payDate string
    )
    '''

    totalIncomeTable = '''
    CREATE TABLE IF NOT EXISTS TotalIncome (
        totalIncome number,
        incomeId number DEFAULT 1
    );
    '''

    populateTotalIncomeTable = '''
    INSERT INTO TotalIncome VALUES (
        {}
    )
    '''.format(totalIncome)

    cursor.execute(ExpensesTable)
    cursor.execute(IncomeTable)
    cursor.execute(totalIncomeTable)
    cursor.execute(populateTotalIncomeTable)
    connect.commit()


def logPay(amount, category, message=""):
    """
    Insert pay record into database based on amount, category,
    and message passed
    """
    date = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    connect = db.connect("test.db")
    cursor = connect.cursor()
    SQL = '''
    INSERT INTO Income VALUES (
         {},
        '{}',
        '{}',
        '{}'
    )
    '''.format(amount, category, message, date)
    SQL2 = '''
    UPDATE TotalIncome
    SET
        TotalIncome = TotalIncome + {}
    '''.format(amount)
    try:
        cursor.execute(SQL)
        cursor.execute(SQL2)
    except:
        print("Couldn't log pay amount. Try again.")
    connect.commit()


def logExpense(amount, category, message=""):
    """
    Inserting record into database based on amount, category,
    and message passed
    """
    date = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    connect = db.connect("test.db")
    cursor = connect.cursor()
    SQL = '''
    INSERT INTO Expenses VALUES (
         {},
        '{}',
        '{}',
        '{}'
    )
    '''.format(amount, category, message, date)
    SQL2 = '''
    UPDATE TotalIncome
    SET
        TotalIncome = TotalIncome - {}
    '''.format(amount)
    cursor.execute(SQL)
    cursor.execute(SQL2)
    connect.commit()


def delete(amount, category, message=""):
    """
    Deleting record based on amount, category, and message
    passed in
    """
    connect = db.connect("test.db")
    cursor = connect.cursor()
    if message and len(message) > 0:
        SQL = '''
        DELETE FROM Expenses WHERE Amount = {} AND Category = '{}' AND Message = '{}'
        '''.format(amount, category, message)
    else:
        SQL = '''
        DELETE FROM Expenses WHERE Amount = {} AND Category = '{}'
        '''.format(amount, category, message)
    try:
        cursor.execute(SQL)
    except:
        print("Please enter all fields. Try again!")
    connect.commit()


def viewExpense(category=None):
    """
    Looking at entries in expenses database
    """
    connect = db.connect("test.db")
    cursor = connect.cursor()
    if category:
        SQL = '''
        SELECT * FROM Expenses WHERE Category = '{}'
        '''.format(category)
        SQLtotal = '''
        SELECT SUM(Amount) FROM Expenses WHERE Category = '{}'
        '''.format(category)
    else:
        SQL = '''
        SELECT * FROM Expenses
        '''
        SQLtotal = '''
        SELECT SUM(Amount) FROM Expenses
        '''.format(category)
    cursor.execute(SQL)
    results = cursor.fetchall()
    cursor.execute(SQLtotal)
    totalAmount = cursor.fetchone()[0]

    return totalAmount, results


def viewPay(category=None):
    """
    Looking at entries in income database
    """
    connect = db.connect("test.db")
    cursor = connect.cursor()
    if category:
        SQL = '''
        SELECT * FROM Income WHERE payCategory = '{}'
        '''.format(category)
        SQLtotal = '''
        SELECT SUM(payAmount) FROM Expenses WHERE payCategory = '{}'
        '''.format(category)
    else:
        SQL = '''
        SELECT * FROM Income
        '''
        SQLtotal = '''
        SELECT SUM(payAmount) FROM Income
        '''.format(category)
    cursor.execute(SQL)
    results = cursor.fetchall()
    cursor.execute(SQLtotal)
    totalAmount = cursor.fetchone()[0]

    return totalAmount, results


def viewTotalIncome():
    connect = db.connect("test.db")
    cursor = connect.cursor()

    SQL = '''
    SELECT * FROM TotalIncome
    '''
    cursor.execute(SQL)
    # results = cursor.fetchall()
    totalIncome = cursor.fetchone()[0]

    return totalIncome
