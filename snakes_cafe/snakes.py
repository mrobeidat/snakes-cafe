print('**************************************\n\n')


print('**welcome to the snakes cafe!** \n**Please see our menu below.**\n**\n**To quit at any time, type "quit"**')

print('**************************************\n\n')


# for food in menu:
#     print(food, '\n--------')
#     for item in menu[food]:
#         print(item)
#         print('')



print('Appetizers')
print('Wings')
print('Cookies')
print('Spring Rolls', '\n'*2)

print('Entrees')
print('-'*9)
print('Salmon')
print('Steak')
print('Meat Tornado')
print('A Literal Garden', '\n'*2)

print('Desserts')
print('-'*9)
print('Ice Cream')
print('Cake')
print('Pie', '\n'*2)

print('Drinks')
print('-'*9)
print('Coffee')
print('Tea')
print('Unicorn Tears', '\n'*4)

menu = {
    'wings': 0,
    'cookies': 0,
    'spring rolls': 0,
    'salmon': 0,
    'steak': 0,
    'meat tornado': 0,
    'a literal garden': 0,
    'ice cream': 0,
    'cake': 0,
    'pie': 0,
    'coffee': 0,
    'tea': 0,
    'unicorn tears': 0
}


while True:
    order = input(
        ' *********************************** \n ** What would you like to order? ** \n *********************************** \n')
    if order == 'quit':
        break
    if order.lower() in menu:
        print('hello')
        menu[order.lower()] += 1
        if menu[order.lower()] == 1:
            print(f'1 order of {order} have been added to your meal')
        else:
            print(
                '**', f'{menu[order.lower()]} order of {order} have been added to your meal', '**')
