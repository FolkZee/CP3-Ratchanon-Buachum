menuList = []
priceList = []

def showBill():
    Total = 0
    print("---- My Food ----")
    for num in range(len(menuList)):
        print(num+1,menuList[num],priceList[num],"THB")
        Total += int(priceList[num])
    print("Total is >",Total,"THB")

while True:
    menuName = input("please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()