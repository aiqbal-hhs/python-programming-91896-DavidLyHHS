from collections import namedtuple
import sys
import time

# Raises an error if the user is not on IDLE
try:
    color = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")

# BUILTIN = Purple
# SYNC = Black
# STRING = Green
# console = Brown
# COMMENT = Red
# KEYWORD = Yellow
# stdout = Blue
# hit = White, Black Background
# ERROR = Black, Red Background
# sel = Black, Grey Background

# Pizza to price
pizza_to_price = {
    "Classic Cheese": 5.00,
    "Classic Veggie": 5.00,
    "Pepperoni": 5.00,
    "Beef & Onion": 5.00,
    "Hawaiian": 5.00,
    "Margherita": 8.50,
    "Chicken Deluxe": 8.50,
    "Meat Lovers": 8.50,
    "Garlic Prawn": 8.50,
    "Americano": 8.50,
    "Supreme": 8.50,
    "Italian": 8.50,
}

# Index of pizza to price
index_to_price = {
    "1": 5.00,
    "2": 5.00,
    "3": 5.00,
    "4": 5.00,
    "5": 5.00,
    "6": 8.50,
    "7": 8.50,
    "8": 8.50,
    "9": 8.50,
    "10": 8.50,
    "11": 8.50,
    "12": 8.50,
}

# Index to pizza
index_to_pizza = {
    "1": "\n- Classic Cheese         $5.00",
    "2": "\n- Classic Veggie         $5.00",
    "3": "\n- Pepperoni              $5.00",
    "4": "\n- Beef & Onion           $5.00",
    "5": "\n- Hawaiian               $5.00",
    "6": "\n- Margherita             $8.50",
    "7": "\n- Chicken Deluxe         $8.50",
    "8": "\n- Meat Lovers            $8.50",
    "9": "\n- Garlic Prawn           $8.50",
    "10": "\n- Americano             $8.50",
    "11": "\n- Supreme               $8.50",
    "12": "\n- Italian               $8.50",
}

# Creates a namedtuple for the pizza menu
PizzaEntry = namedtuple("PizzaEntry", ["index", "pizza", "price"])
# Creates a new list for the pizza options
pizza_options = []
# Appends values to the list in the 'PizzaEntry' namedtuple format
pizza_options.append(PizzaEntry(1, "Classic Cheese", "$5.00"))
pizza_options.append(PizzaEntry(2, "Classic Veggie", "$5.00"))
pizza_options.append(PizzaEntry(3, "Pepperoni", "$5.00"))
pizza_options.append(PizzaEntry(4, "Beef & Onion", "$5.00"))
pizza_options.append(PizzaEntry(5, "Hawaiian", "$5.00"))
pizza_options.append(PizzaEntry(6, "Margherita", "$8.50"))
pizza_options.append(PizzaEntry(7, "Chicken Deluxe", "$8.50"))
pizza_options.append(PizzaEntry(8, "Meat Lovers", "$8.50"))
pizza_options.append(PizzaEntry(9, "Garlic Prawn", "$8.50"))
pizza_options.append(PizzaEntry(10, "Americano", "$8.50"))
pizza_options.append(PizzaEntry(11, "Supreme", "$8.50"))
pizza_options.append(PizzaEntry(12, "Italian", "$8.50\n"))

# Creates a namedtuple for the toppings menu
ToppingEntry = namedtuple("ToppingEntry", ["index", "topping", "price"])
# Creates a new list for the topping options
topping_options = []
# Appends values to the list in the 'ToppingEntry' namedtuple format
topping_options.append(ToppingEntry(1, "Extra Cheese", "$0.50"))
topping_options.append(ToppingEntry(2, "Extra Onion", "$0.50"))
topping_options.append(ToppingEntry(3, "Extra Mushroom", "$0.50"))
topping_options.append(ToppingEntry(4, "Extra Pepperoni", "$0.50"))
topping_options.append(ToppingEntry(5, "Extra Olives", "$0.50"))
topping_options.append(ToppingEntry(6, "Extra Ham", "$0.50"))

# Create an empty list to store the orders

order_list = []

topping = []
order_cost = 0


# Formats the pizza menu using Ijust
def pizza_menu():
    for entry in pizza_options:
        index = str(getattr(entry, "index")).ljust(5)
        pizza = getattr(entry, "pizza").ljust(25)
        price = getattr(entry, "price").ljust(7)
        print("{0}{1}{2}".format(index, pizza, price))


# Formats the pizza menu using Ijust
def topping_menu():
    for entry in topping_options:
        index = str(getattr(entry, "index")).ljust(5)
        topping = getattr(entry, "topping").ljust(25)
        price = getattr(entry, "price").ljust(7)
        print("{0}{1}{2}".format(index, topping, price))


# toppings to price list
index_to_topping = {
    "1": " + Extra Cheese          $0.50",
    "2": " + Extra Onions          $0.50",
    "3": " + Extra Mushroom        $0.50",
    "4": " + Extra Pepperoni       $0.50",
    "5": " + Extra Olives          $0.50",
    "6": " + Extra Ham             $0.50",
}
# Contact information for delivery
contact = {}

color.write("Henderson Pizza Palace\n", "hit")
color.write(
    "\nGood Evening, you are calling Henderson Pizza Palace.\nBelow is"
    " our phone operator, please input the number of your required service.\n",
    "SYNC")


# Prints out menu of functions that the user could input
def menu():
    color.write("\nType: \n", "SYNC")
    color.write("'1' to view phone operator\n", "SYNC")
    color.write("'2' to view pizza menu\n", "SYNC")
    color.write("'3' to order pizza\n", "SYNC")
    color.write("'4' to exit phone operator\n", "SYNC")


# Service menu function
def service_menu(order_cost, topping):
    # Prints out the available choices regarding collection method for the user
    color.write("How would you like the pizza to get to you?\n", "SYNC")
    color.write("'1' Delivery ($3 surcharge)\n", "SYNC")
    color.write("'2' Pick-up\n", "SYNC")
    color.write("'3' to go back to phone operator menu\n", "SYNC")
    # Keeps repeating this code until service_repeat = False
    service_repeat = True
    while service_repeat:
        # User input asking for the collection method
        service_option = input("\nInput here: ").strip()
        # If the user inputs "1" the following code occurs
        if service_option == "1":
            # Tells the user the option they have selected
            color.write("\nService Option: Delivery\n", "STRING")
            # Adds $3 to their final order cost
            order_cost += 3
            # Repeats the code until contact_repeat = False
            contact_repeat = True
            while contact_repeat is True:
                # Try and except is used here to force input an integer 
                try:
                    color.write("\nPlease state your phone number\n", "SYNC")
                    phone_number = int(input("Input here: ").strip())
                except ValueError:
                    color.write("\nPlease enter an integer (ie: a number which"
                                " does not have a decimal part).\n", "COMMENT")
                    continue
                # Adds the phone number into the contact dictionary
                contact["Phone number"] = phone_number
                # Asks the user to input their address and strips their input
                color.write("\nPlease state your address\n", "SYNC")
                address = input("Input here: ").strip()
                # Titles and adds address into contact dictionary
                contact["Address"] = address.title()
                # Asks the user to input their name and strips their input
                color.write("\nPlease state your name\n")
                name = input("Input here: ").strip()
                # Titles and adds the users name into contact dictionary
                contact["Name"] = name.title()
                color.write("\nContact Information:\n", "SYNC")
                # Prints out the contact dictionary for the user to see
                color.write(contact, "STRING")
                print()
                # Keeps repeating this code until information_repeat = False
                information_repeat = True
                while information_repeat is True:
                    color.write(
                        "\nIs your contact information correct?"
                        " (Answer: 'yes' or 'no')\n", "sync"
                        )
                    # Asks user if contact information is correct
                    information = input("Input here: ").strip().lower()
                    # If the user inputs 'no', code will repeat
                    if information == "no" or information == "n":
                        print("\nPlease resubmit your contact information")
                        information_repeat = False
                        continue
                    # If the user inputs 'yes', order menus are printed
                    elif information == "yes" or information == "y":
                        print()
                        information_repeat = False
                        contact_repeat = False
                    # If the user does not input 'yes' or 'no', code will loop
                    else:
                        color.write("\nPlease enter a"
                                    " valid response!\n", "COMMENT")

            order(order_cost)
            service_repeat = False

        # If the user inputs "2", name is asked and menus are printed
        elif service_option == "2":
            # Tells the user the option they have selected
            color.write("\nService Option: Pick-up\n", "STRING")
            # Asks the user to input their name and strips their input
            color.write("\nPlease state your name\n")
            name = input("Input here: ").strip()
            # Titles and adds the users name into contact dictionary
            contact["Name"] = name.title()
            print("")
            # Functions are called for the user to place an order
            order(order_cost)
        # If the user inputs "3", the user will go to the phone operator menu
        elif service_option == "3":
            menu()
            break
        # When if/elif is not met, they will be asked to input a valid number
        else:
            color.write("\nPlease input a valid number\n", "COMMENT")


# Function that takes in the users orders and calculates the price
def order(order_cost):
    order_loop = 0
    # Will continue to run this code until the code breaks
    while True:
        order_loop += 1
        # Prints instructions on what actions are available for the user
        pizza_menu()
        color.write("\nMaximum number of pizzas is 5\n", "STRING")
        color.write("\nOrder using the number next to"
                    " the name of the pizza.", "SYNC")
        color.write("\nTo finish ordering, type 'end'.", "SYNC")
        color.write("\nTo cancel ordering, type 'cancel'.", "SYNC")
        # Asks for user input for their order
        new_order = input("\nInput here: ")
        # If the user inputs "end", contact and order information displayed
        if new_order == "end" or order_loop > 5:
            color.write("\nContact Information:\n", "SYNC")
            color.write(contact, "STRING")
            print("")
            color.write("\nYour order is:\n", "SYNC")
            view_order()
            print("\nYour total order cost is ${:.2f}".format(order_cost))
            print("\nThis total includes any applied surcharges")
            # User input on whether the users order is correct or not
            color.write("\nIs your order correct?"
                        " Please input 'yes' or 'no'\n", "SYNC")
            correct = input("Input here: ").strip().lower()
            # Order confirmed and menu displayed if these inputs are made
            if correct == "yes" or correct == "y":
                color.write(
                    "\nYour order will be ready soon,"
                    " thanks for ordering at Henderson Pizza Palace!\n",
                    "STRING"
                )
                # Clears the order_list
                order_list.clear()
                menu()
                break
            # If the user input is "no", the users order_list will be cleared
            elif correct == "no" or correct == "no":
                order_list.clear()
                order_loop = 0
                print()
        # Checks to see if the user input is in index_to_pizza dictionary
        elif new_order in index_to_pizza:
            # Adds the name of the pizza to the order list
            order_list.append(index_to_pizza.get(new_order))
            # Adds the price of the pizza to the order cost
            order_cost += index_to_price.get(new_order)
            # Displays the topping menu
            print()
            topping_menu()
            # This code will keep repeating until the code breaks
            while True:
                # Asks for user input on any toppings they would like to add
                color.write("\nAdd toppings using the number next"
                            " to the topping name.", "SYNC")
                color.write("\nTo finish adding toppings, type 'end'.", "SYNC")
                topping = input("\nInput here: ").strip().lower()
                # Checks the name of the topping corresponding to the number
                if topping in index_to_topping:
                    # Adds the name of the topping to the order list
                    order_list.append(index_to_topping.get(topping))
                    # Adds 50c to the total order_cost for every topping added
                    order_cost += 0.5
                # Checks for 'end', where order cost will be displayed
                elif topping == "end":
                    print("\nYour current total order"
                          " cost is ${:.2f}".format(order_cost))
                    print()
                    break
                # If the user input is neither if/elif, the code will repeat
                else:
                    color.write(
                        "\nThat is not one of the"
                        " topping options.\n", "COMMENT")
        # Checks to see if the user input is "cancel"
        elif new_order == "cancel":
            # Clears the order list
            order_list.clear()
            # Displays the phone operator menu
            menu()
            break
        # The code will repeat
        else:
            color.write("\nSorry, that is not one"
                        " of the pizza options\n", "COMMENT")


# Function that shows current orders in the order_list
def view_order():
    if len(order_list) > 0:
        for order in order_list:
            print("{}".format(order, topping))
    else:
        color.write("You have no orders yet!", "COMMENT")


# Prints the phone operator menu
menu()

# Run program loop
repeat = True
while repeat is True:

    # Asks for user input on action of phone operator
    option = input("\nInput Here: ").strip()
    print("")

    # If/else statements to check the number that the user has inputted
    # Calls the needed function relating to that number
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
