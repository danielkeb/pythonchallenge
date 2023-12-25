from menu import MENU,resources,profit
#print(MENU['espresso'])

profit = 0.0
is_on=False
def process_coins():
    print("please insert coins")
    q=int(input("how many quarters?: ")) * 0.25
    q+=int(input("how many nickles?: ")) *0.05
    q+=int(input("how many dimes?:")) * 0.2
    q+=int(input("how many pennies?: ")) *0.01

    return q

def is_transaction_success(money_received,drink_cost):
    if money_received>=drink_cost:
        change=float(round(money_received-drink_cost,2))
        print(f"Here is ${change} in change")
        global profit
        profit+=drink_cost
        return False
    else:
        print("Sorry that's not enough money. Money refunded.")
        is_on=True
        return True
def make_coffee(drink_name,order_ingredient):
    for item in order_ingredient:
        resources[item]-=order_ingredient[item]
    print(f"Here is your {drink_name}. Enjoy! ")


def is_sufficient(drink):
    for item in drink:
        if drink[item]>=resources[item]:
            print(f"Sorry there is not enough {item}")
            is_on=True
            return True
    return False


while not is_on:
    choice=input("What you you like? (espresso/latte/cappuccino): ").lower()
    if choice=='off':
        is_on=True
        print("coffee machine off!")

    if choice=='report':
        print(f"water : {resources['water']}ml")
        print(f"milk : {resources['milk']}ml")
        print(f"coffee : {resources['coffee']}g")
        print(f"cost : ${profit}")
    else:
        drink=MENU[choice]
       
        is_sufficient(drink['ingredient'])
        payment=process_coins()
        is_transaction_success(payment,drink["cost"])
        make_coffee(choice,drink["ingredient"])

