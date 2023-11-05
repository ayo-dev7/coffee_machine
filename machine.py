menu_items = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "price": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "price": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "price": 3.0,
    }
}

inventory = {
     "water": 300,
     "milk": 200,
     "coffee": 100,
}

coin_values = {'quarters': 0.25, 'dimes': 0.10, 'nickels': 0.05, 'pennies': 0.01}

earnings = 0

machine_on = True


def check_inventory(order_ingredients):
    return all(inventory[item] >= order_ingredients[item] for item in order_ingredients)


def accept_coins():
    return round(sum(coin_values[coin] * int(input(f"Insert {coin}: ")) for coin in coin_values), 2)


def process_transaction(coins_inserted, item_price):
    if coins_inserted >= item_price:
        change = round(coins_inserted - item_price, 2)
        print(f"Here's your change: ${change}")
        global earnings
        earnings += item_price
        return True
    print("Sorry, the payment is insufficient. Money refunded.")
    return False


def prepare_drink(drink_name, required_ingredients):
    for item in required_ingredients:
        inventory[item] -= required_ingredients[item]
    print(f"Here is your {drink_name}.")


while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        for item, quantity in inventory.items():
            print(f"{item.capitalize()}: {quantity}")
        print(f"Earnings: ${earnings:.2f}")
    else:
        item_details = menu_items.get(choice)
        if item_details and check_inventory(item_details["ingredients"]):
            payment = accept_coins()
            if process_transaction(payment, item_details["price"]):
                prepare_drink(choice, item_details["ingredients"])