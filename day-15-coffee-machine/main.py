from menu import MENU
def compute_money(q,d,n,p):
    """
    Computes the received_money money in dollars given numbers of quarters, dimes, nickkles, and pennies
    """
    return q *.25 + d *.1 + n *.05 + p *.01

def print_report(resources):
    print('Water: {}ml'.format(resources['water']))
    print('Milk: {}ml'.format(resources['milk']))
    print('Cofee: {}g'.format(resources['coffee']))
    print('Money: {}$'.format(resources['money']))

def is_enough_resources(received_money, drink, resources):
    required_money = MENU[drink]['cost']
    required_water = MENU[drink]['ingredients']['water']
    required_milk = MENU[drink]['ingredients']['milk']
    required_coffee = MENU[drink]['ingredients']['coffee']

    if received_money < required_money :
        print('Sorry that\'s not enough money. Money refunded.')
        return False
    elif resources['water'] < required_water:
        print('Sorry there is not enough water.')
        return False
    elif resources['milk'] < required_milk:
        print('Sorry there is not enough milk.')
        return False
    elif resources['coffee'] < required_coffee:
        print('Sorry there is not enough coffee.')
        return False
    else :
        return True

def make_coffee(received_money, drink, resources):
    # print(resources)
    required_money = MENU[drink]['cost']
    required_water = MENU[drink]['ingredients']['water']
    required_milk = MENU[drink]['ingredients']['milk']
    required_coffee = MENU[drink]['ingredients']['coffee']
    resources['water'] -= required_water
    resources['milk'] -= required_milk
    resources['coffee'] -= required_coffee
    resources['money'] += required_money
    change = received_money - required_money
    print('Here is your change:{:05.2f}'.format(change))
    print('Here is your {}, Enjoy!'.format(drink))

def insert_coins():
    print('Please insert coins')
    quarters = int(input('How many quarters?'))
    dimes = int(input('How many dimes?'))
    nickles = int(input('How many nickles?'))
    pennies = int(input('How many pennies?'))
    return compute_money(quarters, dimes, nickles, pennies)

def main():
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0
    }
    drink=input('What would you like?( espresso/latte/cappuccino):')
    while drink != 'off':
        if drink=='report':
                   print_report(resources)
        elif drink=='latte' or drink=='espresso' or drink =='cappuccino':
            received_money = insert_coins()
            if is_enough_resources(received_money, drink, resources):
                make_coffee(received_money, drink, resources)
        else:
            print('Please drink a correct input!!')
        drink=input('What would you like?( espresso/latte/cappuccino):')

if __name__ == "__main__":
    main()
