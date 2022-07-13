from art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    },
    "cold coffee": {
        "ingredients": {
            "water": 150,
            "milk": 60,
            "coffee": 24,
        },
        "cost": 20,
    }
}

profit = 0
resources = {
    "water": 600,
    "milk": 400,
    "coffee": 100,
}


def is_res_suffi(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("how many Re.1 coins?: "))
    total += int(input("how many Rs.2 coins?: ")) * 2
    total += int(input("how many Rs.5 coins?: ")) * 5
    total += int(input("how many Rs.10 coins?: ")) * 10
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is Rs.{change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is you {drink_name} ☕")


print(logo)
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino/cold coffee): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: Rs. {profit}")
    else:
        drink = MENU[choice]
        if is_res_suffi(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


