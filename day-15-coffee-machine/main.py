from menu import MENU
def Compute_Money(q,d,n,p):
    """
    Computes the total money in dollars given numbers of quarters, dimes, nickkles, and pennies
    """
    return q *.25 + d *.1 + n *.05 + p *.01

def main():
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0
    }
    type_coffee=input('What would you like?( espresso/latte/cappuccino):')
    while type_coffee != 'off':
        if type_coffee=='report':
            print('Water: {}ml'.format(resources['water']))
            print('Milk: {}ml'.format(resources['milk']))
            print('Cofee: {}g'.format(resources['coffee']))
            print('Money: {}$'.format(resources['money']))
        elif type_coffee=='latte' or type_coffee=='espresso' or type_coffee =='cappuccino':
            print('Please insert coins')
            quarters = int(input('How many quarters?'))
            dimes = int(input('How many dimes?'))
            nickles = int(input('How many nickles?'))
            pennies = int(input('How many pennies?'))
            total = Compute_Money(quarters, dimes, nickles, pennies)
            required_money = MENU[type_coffee]['cost']
            required_water = MENU[type_coffee]['ingredients']['water']
            required_milk = MENU[type_coffee]['ingredients']['milk']
            required_coffee = MENU[type_coffee]['ingredients']['coffee']
            if total < required_money :
                print('Sorry that\'s not enough money. Money refunded.')
            elif resources['water'] < required_water:
                print('Sorry there is not enough water.')
            elif resources['milk'] < required_milk:
                print('Sorry there is not enough milk.')
            elif resources['coffee'] < required_coffee:
                print('Sorry there is not enough coffee.')
            else:
               resources['water'] -= required_water
               resources['milk'] -= required_milk
               resources['coffee'] -= required_coffee
               resources['money'] += required_money
               change = total - required_money
               print('Here is your change:{:05.2f}'.format(change))
               print('Here is your {}, Enjoy!'.format(type_coffee))
        else:
            print('Please type_coffee a correct input!!')
        type_coffee=input('What would you like?( espresso/latte/cappuccino):')

if __name__ == "__main__":
    main()
