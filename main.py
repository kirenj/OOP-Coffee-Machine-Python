from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
#menu_item = MenuItem()
#MenuItem() class cannot be called into an object as it is directly connected with the Menu() class.
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_continue = True

while machine_continue:
  user_choice = input(f"What would you like? {menu.get_items()}: ")
  
  #Turn off machine by entering the "off" prompt
  if user_choice == 'off':
    machine_continue = False
  elif user_choice == 'report':
    #These are the two Methods for getting the report of items and money
    coffee_maker.report()
    money_machine.report()

  #Check resource sufficient
  else:
    #whatever is the user choice in the Method, we assign it to a variable for later use.
    drink = menu.find_drink(user_choice)
    # resource_sufficient will capture the True or False statement of the is_resource_sufficient method.
    resource_sufficient = coffee_maker.is_resource_sufficient(drink)
    #here drink value will have to be mentioned as 'not None' or this will through an error.
    if resource_sufficient is True and drink is not None:
      #the cost attribute is part of the MenuItem class, but as this class cannot be assigned to an object, we use the drink variable where 'menu' object was already defined. Then we can call in the cost attribute.
      payment = money_machine.make_payment(drink.cost)
      # asks the user to input the coins and calculates based on the drinks cost.
      if payment is True:
        # the make_coffee method, makes the coffee and deduct the values from the resources
        coffee_maker.make_coffee(drink)
      
