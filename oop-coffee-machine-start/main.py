from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
payment_machine = MoneyMachine()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_machine.report()
        payment_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink) and payment_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
