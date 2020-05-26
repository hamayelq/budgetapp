from docopt import docopt
from tabulate import tabulate
from spent import *


usage = '''
Expense Tracker CLI

Usage:
    spent_driver.py init
    spent_driver.py view [<viewCategory>]
    spent_driver.py <amount> <category> [<message>]
'''


args = docopt(usage)


if args['init']:
    init()
    print("User Profile Created")


if args['view']:
    category = args['<viewCategory>']
    amount, results = view(category)
    print("Total Expenses: " + str(amount))
    print(tabulate(results))


if args['<amount>']:
    try:
        amount = float(args['<amount>'])
        log(amount, args['<category>'], args['<message>'])
    except:
        print('Error\n')
        print(usage)
