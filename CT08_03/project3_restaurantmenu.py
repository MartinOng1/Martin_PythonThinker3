menu = {
    "burger" : 5.50,
    "fries" : 3.00,
    "coke" : 2.00,
    "ice cream" : 4.00,
    "nuggets" : 6.00
}

print("Here is our menu:")
for item in menu:
    print(f"{item.title()}: ${menu[item]}")

cart = {}
wallet = 10
order = ""

while order != "no more":
    order = input('What would you like to order? (Type "No more" to stop): ').lower().strip()
    if order[0:6] == "remove":
        if order[7:] in cart:
            del cart[order[7:]]
            wallet += menu[order[7:]]
            print(f"{order[7:].title()} was removed from your order. Your current balance is ${wallet}.")
        else:
            print(f"That item is not in your order.")
    elif order in menu:
        print(f"{order.title()}: ${menu[order]}")
        addcart = ""
        while addcart not in ["Y", "N"]:
            addcart = input("Would you like to add that to your order? (Y/N): ").upper().strip()
            if addcart == "Y":
                if menu[order] < wallet:
                    if order not in cart:
                        cart[order] = menu[order]
                    else:
                        cart[order] += menu[order]
                    wallet -= menu[order]
                    print(f"The item was successfully added to your order. Your current balance is ${wallet}.")
                else:
                    print(f"You do not have enough money for that item. Your current balance is ${wallet}.")
            elif addcart == "N":
                print("The item was not added to your order.")
            else:
                print('Please type "Y" or "N" only.')
    elif order == "no more":
        totalcost = 0
        print()
        print("--- Order Summary ---")
        for item in cart:
            print(f"{item.title()}: ${cart[item]}")
            totalcost += cart[item]
        print()
        print("---------------------")
        print(f"Total: ${totalcost}")
        print(f"Your remaining balance is ${wallet}")
        print(f"Enjoy your meal!")
    else:
        print("That item is unavailable.")


# What would you like to order? remove Fries
# Fries has been removed from your order.

# What would you like to order? remove Burger
# Burger is not in your order.
# --- Order Summary ---
# Fries:          $3.00
# Burger:         $5.00
# Apple Pie:      $2.50

# ---------------------
# Total: $10.50

# Your total bill is $10.50. Enjoy your meal!
