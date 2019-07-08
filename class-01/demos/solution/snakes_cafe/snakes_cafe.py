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

print(welcome, menu)

while True:
    order = input(order_prompt)

    if order == 'quit':
        break
    
    print('** x order of ' + order + ' have been added to your meal **')
