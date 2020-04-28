menuList = []

def showBill():
    Total = 0
    print("---- My Food ----")
    for num in range(len(menuList)):
        print(num+1,menuList[num][0],menuList[num][1],"THB")
        Total += int(menuList[num][1])
    print("Total is >",Total,"THB")

while True:
    menuName = input("please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName,menuPrice])
showBill()