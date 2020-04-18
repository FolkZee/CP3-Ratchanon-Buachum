UsernameInput = input("Username : ")
PasswordInput = input("Password : ")
if UsernameInput == "user123" and PasswordInput == "1111":
    print("Done!")
    print("Welcome to 123computer")
    print("-"*23)
    print("Product list")
    print("-"*23)
    print("1.Monitor 23.5 inch    3500 THB")
    print("2.Headphone            900  THB")
    print("3.mouse                1200 THB")
    print("4.keyboard             3700 THB")
    UserSelect = int(input("add to cart : "))
    if UserSelect == 1:
        Numberofpieces = int(input("pieces >> "))
        if Numberofpieces >= 1 :
            print("Tolal is",3500*Numberofpieces,"THB")
    elif UserSelect == 2:
        Numberofpieces = int(input("pieces >> "))
        if Numberofpieces >= 1 :
            print("Tolal is",900*Numberofpieces,"THB")
    elif UserSelect == 3:
        Numberofpieces = int(input("pieces >> "))
        if Numberofpieces >= 1 :
            print("Tolal is",1200*Numberofpieces,"THB")
    elif UserSelect == 4:
        Numberofpieces = int(input("pieces >> "))
        if Numberofpieces >= 1 :
            print("Tolal is",3700*Numberofpieces,"THB")
else:
    print("Wrong!!!")