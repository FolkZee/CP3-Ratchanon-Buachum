def login():
    UsernameInput = input("Username : ")
    PasswordInput = input("Password : ")
    if UsernameInput == "User123" and PasswordInput == "1111":
        return True
    else:
        return False
def showMenu():
    print("Done!")
    print("Welcome to 123shop")
    print("-"*23)
    print("Product list")
    print("-"*23)
    print("1. Vat Calculator")
    print("2. Price Calculator")
def menuSelect():
    UserSelect = int(input(">>"))
    return UserSelect
def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat/100)
    return result
def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)
if login():
    showMenu()
    while True:
        menu = menuSelect()
        if menu == 1:
            Price = int(input("Product Price : "))
            print(vatCalculator(Price),"THB")
            break
        elif menu == 2:
            print(priceCalculator(),"THB")
            break
        else:
            print("try again")
else:
    print("Wrong!!!")