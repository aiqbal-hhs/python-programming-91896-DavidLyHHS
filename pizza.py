from collections import namedtuple
import sys
import time

# This code checks 
try:
    color = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")

#BUILTIN = Purple
#SYNC = Black
#STRING = Green
#console = Brown
#COMMENT = Red
#KEYWORD = Yellow
#stdout = Blue
#hit = White, Black Background
#ERROR = Black, Red Background
#sel = Black, Grey Background

# Pizza to price
pizza_to_price = {'Classic Cheese': 5.00, 'Classic Veggie': 5.00, 'Pepperoni': 5.00, 'Beef & Onion': 5.00, 'Hawaiian': 5.00, 'Margherita': 8.50, 'Chicken Deluxe': 8.50, 'Meat Lovers': 8.50, 'Garlic Prawn': 8.50, 'Americano': 8.50, 'Supreme': 8.50, 'Italian': 8.50,}

# Index of pizza to price
index_to_price = {'1': 5.00, '2': 5.00, '3': 5.00, '4': 5.00, '5': 5.00, '6': 8.50, '7': 8.50, '8': 8.50, '9': 8.50, '10': 8.50, '11': 8.50, '12': 8.50,}

# Index to pizza
index_to_pizza = {'1': '\n- Classic Cheese', '2': '\n- Classic Veggie', '3': '\n- Pepperoni', '4': '\n- Beef & Onion', '5': '\n- Hawaiian', '6': '\n- Margherita', '7': '\n- Chicken Deluxe', '8': '\n- Meat Lovers', '9': '\n- Garlic Prawn', '10': '\n- Americano', '11': '\n- Supreme', '12': '\n- Italian'}

# Pizza Menu 
MenuEntry = namedtuple('MenuEntry', ['index','pizza','price'])
pizza_options = []
pizza_options.append(MenuEntry(1, 'Classic Cheese', '$5.00'))
pizza_options.append(MenuEntry(2, 'Classic Veggie', '$5.00'))
pizza_options.append(MenuEntry(3, 'Pepperoni', '$5.00'))
pizza_options.append(MenuEntry(4, 'Beef & Onion', '$5.00'))
pizza_options.append(MenuEntry(5, 'Hawaiian', '$5.00'))
pizza_options.append(MenuEntry(6, 'Margherita', '$8.50'))
pizza_options.append(MenuEntry(7, 'Chicken Deluxe', '$8.50'))
pizza_options.append(MenuEntry(8, 'Meat Lovers', '$8.50'))
pizza_options.append(MenuEntry(9, 'Garlic Prawn', '$8.50'))
pizza_options.append(MenuEntry(10, 'Americano', '$8.50'))
pizza_options.append(MenuEntry(11, 'Supreme', '$8.50'))
pizza_options.append(MenuEntry(12, 'Italian', '$8.50\n'))

# Toppings Menu
ToppingEntry = namedtuple('ToppingEntry', ['index','topping','price'])
topping_options = []
topping_options.append(ToppingEntry(1, 'Extra Cheese', '$0.50'))
topping_options.append(ToppingEntry(2, 'Extra Onion', '$0.50'))
topping_options.append(ToppingEntry(3, 'Extra Mushroom', '$0.50'))
topping_options.append(ToppingEntry(4, 'Extra Pepperoni', '$0.50'))
topping_options.append(ToppingEntry(5, 'Extra Olives', '$0.50'))
topping_options.append(ToppingEntry(6, 'Extra Ham', '$0.50'))

# Create an empty list to store the orders

order_list = []

topping = []
order_cost = 0

# Formats the pizza menu
def pizza_menu():
    for entry in pizza_options:
        index = str(getattr(entry,'index')).ljust(5)
        pizza = getattr(entry,'pizza').ljust(25)
        price = getattr(entry,'price').ljust(7)
        print('{0}{1}{2}'.format(index,pizza,price))

# Formats the pizza menu
def topping_menu():
    for entry in topping_options:
        index = str(getattr(entry,'index')).ljust(5)
        topping = getattr(entry,'topping').ljust(25)
        price = getattr(entry,'price').ljust(7)
        print('{0}{1}{2}'.format(index,topping,price))
    
# toppings to price list
index_to_topping = {'1': ' + Extra Cheese', '2': ' + Extra Onions', '3': ' + Extra Mushroom', '4': ' + Extra Pepperoni', '5': ' + Extra Olives', '6': ' + Extra Ham'}
# Contact information for delivery
contact = {}

color.write("Henderson Pizza Palace\n", "hit")
color.write("\nGood Evening, you are calling Henderson Pizza Palace.\nBelow is our phone operator, please input the number of your required service.\n", "SYNC")

# Menu function prints out the instructions for the user so they can use a mode option for the Henderson Pizza Palace service.
def menu():
  """Prints out the instructions for the user so they can use a mode option for the Henderson Pizza Palace service."""
  color.write("\nType: \n", "SYNC")
  color.write("'1' to view phone operator\n", "SYNC")
  color.write("'2' to view pizza menu\n", "SYNC")
  color.write("'3' to order pizza\n", "SYNC")
  color.write("'4' to cancel ordering\n", "SYNC")

# Menu function prints out the instructions for the user so they can use a service option for the Henderson Pizza Palace service.
def service_menu(order_cost, topping):
  """Prints out the instructions for the user so they can use a mode option for the Henderson Pizza Palace service."""
  color.write("How would you like the pizza to get to you?\n", "SYNC")
  color.write("'1' Delivery ($3 surcharge)\n", "SYNC")
  color.write("'2' Pick-up\n", "SYNC")
  color.write("'3' to go back menu\n", "SYNC")
  service_repeat = True
  while service_repeat:
      service_option = input("\nInput here: ").strip()
      # Asks the user to input address and phone number
      # Will ask if contact information is correct
      # Will remove contact information and repeat if user inputs "no"
      if service_option == "1":
        color.write("\nService Option: Delivery\n", "STRING")
        order_cost += 3
        contact_repeat = True
        while contact_repeat == True:
          try:
            color.write("\nPlease state your phone number\n", "SYNC")
            phone_number = int(input("Input here: ").strip())
          except ValueError:
            color.write("\nPlease input integer only...\n", "COMMENT")
            continue
          contact['Phone number'] = phone_number
          color.write("\nPlease state your address\n", "SYNC")
          address = input("Input here: ").strip()
          contact['Address'] = address.title()
          color.write("\nPlease state your name\n")
          name = input("Input here: ").strip()
          contact['Name'] = name.title()
          color.write("\nContact Information:\n", "SYNC")
          color.write(contact, "STRING")
          print()
          color.write("\nIs your contact information correct? (Answer: 'yes' or 'no')\n", "sync")
          information = input("Input here: ").strip().lower()
          if information == "no":
            print("\nPlease resubmit your contact information")
            continue
          elif information == "yes":
            print()
            pizza_menu()
            topping_menu()
            contact_repeat = False
            break
          else:
            color.write("Please enter a valid response!", "COMMENT")

        order(order_cost)
        service_repeat = False
            
      elif service_option == "2":
        color.write("\nService Option: Pick-up\n", "STRING")
        color.write("\nPlease state your name\n")
        name = input("Input here: ").strip()
        contact['Name'] = name.title()
        print("")
        pizza_menu()
        topping_menu()
        order(order_cost)
      elif service_option == "3":
        menu()
        break
      else:
        color.write("\nPlease input a valid number\n", "COMMENT")

# Function that takes in the users orders 
def order(order_cost):
  while True:
    color.write("\nOrder using the number next to the name of the pizza.", "SYNC")
    color.write("\nTo finish ordering, type 'end'.", "SYNC")
    color.write("\nTo cancel ordering, type 'cancel'.", "SYNC")
    new_order = input("\nInput here: ")
    if new_order == "end":
        color.write("\nContact Information:\n", "SYNC")
        color.write(contact, "STRING")
        print("")
        color.write("\nYour order is:\n", "SYNC")
        view_order()
        print("\nYour total order cost is ${}".format(order_cost))
        color.write("\nIs your order correct? Please input 'yes' or 'no'\n", "SYNC")
        correct = input("Input here: ").strip().lower()
        if correct == "yes":
            color.write("\nYour order will be ready soon! Thanks for ordering at Henderson Pizza Palace!\n", "STRING")
            order_list.clear()
            menu()
            break
        elif correct == "no":
            order_list.clear()
    elif new_order in index_to_pizza:
        order_list.append(index_to_pizza.get(new_order))
        order_cost += index_to_price.get(new_order)
        while True:
            color.write("\nAdd toppings using the number next to the name of the topping.", "SYNC")
            color.write("\nTo finish adding toppings, type 'end'.", "SYNC")
            topping = input("\nInput here: ").strip()
            if topping in index_to_topping:
                order_list.append(index_to_topping.get(topping))
                order_cost += 0.5
            elif topping == "end":
                print("\nYour current total order cost is ${}".format(order_cost))
                break
            else:
                color.write("\nThat is not one of the topping options!\n", "COMMENT")
    elif new_order == "cancel":
        order_list.clear()
        menu()
        break
    else:
        color.write("\nSorry, that is not one of the pizza options\n", "COMMENT")

# Function that shows current orders in the order_list
def view_order():
  if len(order_list) > 0:
    for order in order_list:
      print("{}".format(order, topping))
  else:
    color.write("You have no orders yet!", "COMMENT")

# Print menu
menu()

# Run program loop
repeat = True
while repeat == True:

  # Ask user for input and
  option = input("\nInput Here: ").strip()
  print("")

  # Check input and run the chosen function
  if option == "1":
    menu()
  elif option == "2":
    pizza_menu()
    topping_menu()
    time.sleep(2)
    menu()
  elif option == "3":
    service_menu(order_cost, topping)
  elif option == "4":
    color.write("Thanks for buying from Henderson Pizza Palace!", "STRING")
    repeat = False
  else:
    color.write("That wasn't an option\n", "COMMENT")
