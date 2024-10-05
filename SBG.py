from datetime import datetime

# This line imports the datetime module, which is used to work with dates and times.

name = input("Enter your name: ")

# This line prompts the user to enter their name and stores the input in the 'name' variable.

items_list = '''
Rice      Rs = 20/kg
Sugar     Rs = 30/kg
Salt      Rs = 20/kg
Oil       Rs = 80/ltr
Paneer    Rs = 110/kg
Maggi     Rs = 50/each
Colgate   Rs = 85/each
Lays      Rs = 10/each
'''

# This block defines a string variable 'items_list', which contains a list of available items with their respective prices.

price = 0
pricelist = []
totalprice = 0

# These lines initialize various variables that will be used to store data about the items the user selects, their quantities, and the total price.

finalamount = 0
ilist = []
qlist = []
plist = []

items = {'rice': 20, 'sugar': 30, 'salt': 20, 'oil': 80, 'paneer': 110, 'maggi': 50, 'colgate': 85, 'lays': 10}

# This line defines a dictionary called 'items' that maps item names to their respective prices.

option = int(input('For the list of items, press 1: '))

# This line prompts the user to input an option and converts it to an integer.

if option == 1:
    print(items_list)

# If the user entered 1, it prints the list of available items from the 'items_list' variable.

for i in range(len(items)):

    # This line starts a loop to iterate over the available items.

    inp1 = int(input("If you want to buy, press 1 or press 2 to exit: "))

    # It prompts the user to choose whether they want to buy items (1) or exit (2).

    if inp1 == 2:
        break

    # If the user enters 2, the loop breaks, ending the item selection process.

    if inp1 == 1:
        item = input("Enter your item: ")
        quantity = int(input('Enter quantity: '))

        # If the user enters 1, they are prompted to enter the item name and its quantity.

        if item.lower() in items.keys():
            price = quantity * items[item.lower()]
            pricelist.append((item, quantity, items[item.lower()], price))

            # It checks if the entered item exists in the 'items' dictionary. If it does, it calculates the price and appends the information to 'pricelist'.

            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)

            # It updates the 'totalprice', 'ilist', 'qlist', and 'plist' with the information about the selected item.

        else:
            print("Sorry, the item is unavailable")

        # If the entered item is not in the 'items' dictionary, it informs the user that the item is unavailable.

    else:
        print("You entered the wrong number")

    # If the user enters a number other than 1 or 2, it informs them that they entered the wrong number.

gst = (totalprice * 5) / 100
finalamount = gst + totalprice

# It calculates the GST (Goods and Services Tax) and adds it to the 'totalprice' to compute the 'finalamount'.

inp = input("Can I bill the items? Yes or No: ")

# It prompts the user to confirm whether they want to generate a bill or not.

if inp.lower() == 'yes' and finalamount != 0:

    # If the user enters 'yes' and 'finalamount' is not zero, it proceeds with generating the bill.

    print(25 * '=', "Manu Supermarket", 25 * '=')
    print(28 * ' ', "Rajahmundry")
    print("Name:", name, 30 * " ", "Date:", datetime.now())
    print(75 * "-")
    print("S.No", 6 * " ", 'Items', 10 * " ", 'Quantity', 5 * " ", 'Price')

    # It starts printing the bill with headers like the supermarket name, location, customer name, and date.

    for i in range(len(pricelist)):
        print((i + 1), 8 * ' ', ilist[i], 12 * ' ', qlist[i], 11 * " ", plist[i])

    # It loops through the items in the 'pricelist' and prints the item number, name, quantity, and price.

    print(75 * "-")
    print(50 * " ", 'Total Amount:', 'Rs', totalprice)
    print("GST Amount", 51 * " ", 'Rs', gst)
    print(75 * "-")
    print(50 * " ", 'Final Amount:', 'Rs', finalamount)
    print(75 * "-")
    print(25 * " ", 'Thanks for visiting')
    print(75 * "-")
