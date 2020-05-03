from tkinter import *
from tkinter import messagebox
import math

def cal(event):
    try:
        BMI = (float(textboxWeight.get())/math.pow(float(textboxHight.get())/100,2))
        if BMI >= 30:
            labelResult1.configure(text=int(BMI))
            labelResult2.configure(text="อ้วนมาก",fg='brown')
        elif BMI >= 25:
            labelResult1.configure(text=int(BMI))
            labelResult2.configure(text="อ้วน",fg='red')
        elif BMI >= 23:
            labelResult1.configure(text=int(BMI))
            labelResult2.configure(text="น้ำหนักเกิน",fg='yellow')
        elif BMI >= 18.6:
            labelResult1.configure(text=int(BMI))
            labelResult2.configure(text="น้ำหนักปกติ เหมาะสม",fg='green')
        else:
            labelResult1.configure(text=int(BMI))
            labelResult2.configure(text="ผอมเกินไป",fg='red')
    except:
        messagebox.showerror("ERROR!!!", "ใส่เฉพาะตัวเลขเท่านั้น")

mainWindow = Tk()
labelHight = Label(mainWindow,text="ส่วนสูง", font=('Courier New',18))
labelHight.grid(row=0,column=0)
textboxHight = Entry(mainWindow, font=('Courier New',18))
textboxHight.grid(row=0,column=1)
labelHightUnit = Label(mainWindow,text="เซนติเมตร", font=('Courier New',18))
labelHightUnit.grid(row=0,column=2)
labelWeight = Label(mainWindow,text="น้ำหนัก", font=('Courier New',18))
labelWeight.grid(row=1,column=0)
textboxWeight = Entry(mainWindow, font=('Courier',18))
textboxWeight.grid(row=1,column=1)
labelWeightUnit = Label(mainWindow,text="กิโลกรัม", font=('Courier New',18))
labelWeightUnit.grid(row=1,column=2)
calButton = Button(mainWindow,text="คำนวน", font=('Courier New',18),bg='green',fg='white')
calButton.bind('<Button-1>',cal)
calButton.grid(row=2,column=1)
labelResult = Label(mainWindow,text="BMI = ", font=('Courier New',18))
labelResult.grid(row=3,column=0)
labelResult1 = Label(mainWindow,text="", font=('Courier New',18))
labelResult1.grid(row=3,column=1)
labelResult2 = Label(mainWindow,text="", font=('Courier New',24))
labelResult2.grid(row=4,column=1)
mainWindow.mainloop()