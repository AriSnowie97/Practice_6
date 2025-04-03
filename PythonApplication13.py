def check_access():
    age = int(input("Enter your age: "))
    if age < 18:
        print("Access denied!")
        return
    print("Access granted!")

def check_stock():
    stock_quantity = 20
    ordered_quantity = int(input("Enter the quantity of goods to order: "))
    if ordered_quantity <= 0:
        print("Error: incorrect quantity!")
        return
    if ordered_quantity > stock_quantity:
        print("Not enough goods in stock!")
        return
    print("Your order is accepted!")

def check_password():
    password = input("Enter your password: ")
    if len(password) < 8:
        print("Password too short!")
        return
    if password.lower() in ["password", "12345678"]:
        print("Password too simple!")
        return
    print("Access granted!")

def check_temperature():
    temperature = float(input("Enter the room temperature (C): "))
    if temperature < 16:
        print("Temperature too low! Turn on the heater.")
        return
    if temperature > 28:
        print("Temperature too high! Turn on the air conditioner.")
        return
    print("Temperature is comfortable.")

def check_account_topup():
    amount = float(input("Enter the top-up amount (UAH): "))
    if amount < 10:
        print("Minimum top-up amount is 10 UAH!")
        return
    if amount > 3000:
        print("Top-up amount is too large!")
        return
    print(f"Top-up of {amount} UAH completed successfully!")
check_account_topup()
check_temperature()
check_password()
check_stock()
check_access()