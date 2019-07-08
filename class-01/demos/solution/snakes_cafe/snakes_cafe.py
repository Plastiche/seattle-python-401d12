welcome = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
"""

order_prompt = """
***********************************
** What would you like to order? **
***********************************
"""

menu = """
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
"""



items = {
    'Wings' : 0,
    'Cookies' : 0,
    'Spring Rolls' : 0,
    'Salmon' : 0,
    'Steak' : 0,
    'Meat Tornado' : 0,
    'A Literal Garden' : 0,
    'Ice Cream' : 0,
    'Cake' : 0,
    'Pie' : 0,
    'Coffee' : 0,
    'Tea' : 0,
    'Unicorn Tears' : 0,
}
print(welcome, menu)

while True:
    order = input(order_prompt)

    if order == 'quit':
        break

    if order in items:
        items[order] += 1
        print(f'** {items[order]} order of {order} have been added to your meal **')
    else:
        print('ruh roh')
