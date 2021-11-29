from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

drink_ordered = input("What would you like to have?({}):".format(menu.get_items()))

while drink_ordered != "off":
    if drink_ordered == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(drink_ordered)
        if drink==None:
            print("Please enter a correct drink")
        else:
            if money_machine.make_payment(drink.cost) and coffee_maker.is_resource_sufficient(drink):
                coffee_maker.make_coffee(drink)
    drink_ordered = input("What would you like to have?({}):".format(menu.get_items()))

