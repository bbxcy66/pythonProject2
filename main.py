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

money_box = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO 4.check resources sufficent
def if_sufficient(order_in):
    for i in order_in:
        if order_in[i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True


# TODO 5.Process coins

def process_coin():
    print('Please insert coins:')
    coins = int(input('how many quarters?:')) * 0.25
    coins += int(input('how many dimes?:')) * 0.10
    coins += int(input('how many nickles?:')) * 0.05
    coins += int(input('how many pennies?:')) * 0.01
    return coins


# TODO 6.check transaction successful

def transcation_successful(coins, price):
    if coins >= price:
        change = round(coins - price, 2)
        print(f'Here is ${change} in change')
        global money_box
        money_box += price
        return True
    print("Sorry that's not enough money. Money refunded")
    return False


def make_coffee(product_name, order_in):
    ''' deduct required ingredients form resources'''
    for i in order_in:
        resources[i] -= order_in[i]
    print(f'Here is your {product_name}☕️, have a wonderful day😊')


is_on = True
while is_on:
    order = input("What Would you like today? (espresso/latte/cappuccino)")
    if order == "off":
        is_on = False
    if order == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money_box}")
    else:
        drink = MENU[order]
        if if_sufficient(drink["ingredients"]):
            cash = process_coin()
            if transcation_successful(cash, drink['cost']):
                make_coffee(order, drink['ingredients'])

