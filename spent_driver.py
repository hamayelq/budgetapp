from docopt import docopt
from tabulate import tabulate
from spent import *


usage = '''
Expense Tracker CLI

Usage:
    spent_driver.py init <totalIncome>
    spent_driver.py viewtotal
    spent_driver.py viewexpense [<viewCategory>]
    spent_driver.py viewpay [<viewPayCategory>]
    spent_driver.py delete <amount> <category> [<message>]
    spent_driver.py logexpense <amount> <category> [<message>]
    spent_driver.py logpay <amount> <category> [<message>]
'''


args = docopt(usage)


if args['init']:
    totalIncome = args['<totalIncome>']
    init(totalIncome)
    print("User profile created with total income = {}".format(totalIncome))

if args['viewtotal']:
    print("Total Income = {}".format(viewTotalIncome()))

if args['viewexpense']:
    category = args['<viewCategory>']
    amount, results = viewExpense(category)
    print("Total Expenses: " + str(amount))
    print(tabulate(results))


if args['viewpay']:
    category = args['<viewCategory>']
    amount, results = viewPay(category)
    print("Total Income/Savings: " + str(amount))
    print(tabulate(results))


if args['logpay']:
    try:
        amount = float(args['<amount>'])
        logPay(amount, args['<category>'], args['<message>'])
    except:
        print('Error')
        print(usage)


if args['logexpense']:
    try:
        amount = float(args['<amount>'])
        logExpense(amount, args['<category>'], args['<message>'])
    except:
        print('Error')
        print(usage)


if args['delete']:
    amount = float(args['<amount>'])
    delete(amount, args['<category>'], args['<message>'])
    if(args['<message>']):
        print("Expense of amount ${}, with category {} and message '{}' deleted.".format(
            str(amount), args['<category>'], args['<message>']))
    else:
        print("Expense of amount ${} and category {} deleted.".format(
            str(amount), args['<category>']))
