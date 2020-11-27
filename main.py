MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

profit = 0
coffee_type = ["express", "latte", "cappuccino"]
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def coffee_maker(drink_type, drink_ingredients):
    """We will deduct the required ingredients from the inventory"""
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_type} ☕")


def is_transaction_successful(money_in, cost):
    """check if user has enough money."""
    if money_in >= cost:
        global profit
        profit += cost
        change = round(money_in - cost, 2)
        print(f"Thank you, here is your change: ${change}")
        return True
    else:
        print("Money inserted is not enough, refunding money")
        return False


def is_resources_sufficient(order_ingredient):
    """Check if we have enough ingredients for the order."""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry we do not have enough {item}.")
            return False
    return True


def process_coins():
    """We will be returning total amount inserted by the user."""
    print("Insert Coins")
    total = int(input("How Many Quarters?: ")) * 0.25
    total += int(input("How Many dimes?: ")) * 0.10
    total += int(input("How Many nickles?: ")) * 0.05
    total += int(input("How Many pennies?: ")) * 0.01
    return total


# variable if machine is on
is_on = True
while is_on:
    # variable to keep the prompt
    choice = input("What would you like? (express/latte/cappuccino) : ").lower()
    if choice in coffee_type:
        drink = MENU[choice]
        # we will call is_resources_sufficient to check our stock
        if is_resources_sufficient(drink["ingredients"]):
            # if we enough resource, we will head to next step
            # We first calculate all the money inserted
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                coffee_maker(choice, drink["ingredients"])
    else:
        print(f"Sorry, we do not have {choice}")
