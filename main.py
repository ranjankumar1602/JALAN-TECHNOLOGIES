MENU = {
    "espresso": {
        "ingredients": {
            "milk": 60,
            "cream": 75,
            "latte": 100,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "milk": 80,
            "cream": 90,
            "latte" : 125,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "milk": 100,
            "cream": 125,
            "latte": 150,
        },
        "cost": 3.0,
    }
}

resources = {
    "milk": 1000,
    "cream": 1000,
    "latte": 2000,
}

profit = 0


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino/off to exit): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Milk: {resources['milk']}ml")
        print(f"Cream: {resources['cream']}ml")
        print(f"Latte: {resources['latte']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


