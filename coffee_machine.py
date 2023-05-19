MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

print("Control commands: [report], [off]\n")


def report_resources():
    print(f"Water: {resources['water']}\nMilk: {resources['milk']}"
          f"\nCoffee: {resources['coffee']}\nMoney: ${'{:.2f}'.format(resources['money'])}\n")


def check_ingredients(coffee):
    for i in MENU[coffee]["ingredients"]:
        if resources[i] < MENU[coffee]["ingredients"][i]:
            print(f"Sorry, there is not enough {i}.\n")
            use()


def make_coffee(coffee):
    for i in MENU[coffee]["ingredients"]:
        resources[i] -= MENU[coffee]["ingredients"][i]


def insert_coins():
    print("\nInsert coins")
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.10
    nickles = float(input("How many nickles?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01
    return quarters + dimes + nickles + pennies


def transaction(coffee, payment):
    if payment >= MENU[coffee]["cost"]:
        change = payment - MENU[coffee]["cost"]
        resources["money"] += MENU[coffee]["cost"]
        print(f"\nYour change: {round(change, 2)}\nEnjoy your {coffee}\n")
        return 1
    else:
        print("Not enough money. And I'm keeping it 😏\n")
        resources["money"] += payment


def use():
    choice = input(f"What would you like to drink?\nEspresso: ${'{:.2f}'.format(MENU['espresso']['cost'])}\n"
                   f"Latte: ${'{:.2f}'.format(MENU['latte']['cost'])}\n"
                   f"Cappuccino: ${'{:.2f}'.format(MENU['cappuccino']['cost'])}\n\nEnter: ").lower()
    if choice == "report":
        report_resources()
        use()
    elif choice == "off":
        print("Bye.")
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        check_ingredients(choice)
        if transaction(choice, insert_coins()) == 1:
            make_coffee(choice)
        use()
    else:
        print("Invalid command. Try again.\n")
        use()


use()















