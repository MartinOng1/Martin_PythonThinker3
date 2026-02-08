menu = {
    "notebook" : 2.50,
    "pencil" : 0.50,
    "pen" : 1.00,
    "ruler" : 1.50,
    "eraser" : 0.50,
    "writing pad" : 2.50,
    "marker" : 2.00,
    "glue" : 3.00,
    "calculator" : 35.00
}
customer_order = {}

for i in menu:
    print(f"{i}: ${menu[i]}0")

while True:
    print()
    order = input("What would you like to order?: ").strip().lower()
    if order in menu:
        print(f"{order}: ${menu[order]}0")
        while True:
            addorder = input("Add to cart? (Y/N): ").strip().upper()
            if addorder == "Y":
                while True:
                    quantityorder = input(f"How many {order}s would you like to buy?: ").strip()
                    if quantityorder.isnumeric():
                        if order not in customer_order:
                            customer_order[order] = {"quantity" : round(int(quantityorder)), "cost" : menu[order]}
                        else:
                            # suggestions: you could also use customer_order[order]["quantity"] += round(int(quantityorder))
                            customer_order[order] = {"quantity" : customer_order[order]["quantity"]+round(int(quantityorder)), "cost" : menu[order]}
                        print("The item successfully added to your order.")
                        break
                    else:
                        print("Please enter a numeric value only.")
                break
            elif addorder == "N":
                print("Item was not added to cart.")
                break
            else:
                print('Please type "Y" or "N" only.')
    elif order == "no more":
        print()
        cost = 0
        for item in customer_order:
            cost += customer_order[item]["quantity"]*customer_order[item]["cost"]
            # take note of the quotes you used in the dictionary, you cannot have a "" inside a ""
            # adding zero is ok for this case but a safer waywould to be using :.2f
            # suggestion: print(f"{customer_order[item]['quantity']} x {item}: ${customer_order[item]['cost'] * customer_order[item]['quantity']:.2f}")
            print(f"{customer_order[item]["quantity"]}x {item}: ${customer_order[item]["cost"]*customer_order[item]["quantity"]}0")
        if cost >= 20:
            cost *= 0.9
            print("Since you exceeded a cost of $20, you availed of a 10 percent discount on your entire purchase!")
        print(f"Your total cost is ${round(cost, 2)}")
        break
    else:
        print("The item is unavailable.")