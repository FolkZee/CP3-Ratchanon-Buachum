systemMenu = {"ข้าวเปล่า":10,"ข้าวหน้าเนื้อ":150,"กะเพราไก้":175,"กะเพราไก่ไข่ดาว":200}
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
        menuList.append([menuName,systemMenu[menuName]])
showBill()