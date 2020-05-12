from typing import List
from forex_python.converter import CurrencyRates
from tkinter import *
from tkinter import messagebox
import datetime

c = CurrencyRates()
currency_list = c.get_rates("")


def currency_converter(event):
    try:
        result = c.convert(first_selected_opt.get(), second_selected_opt.get(), int(textbox_amount.get()))
        label_first_currency.configure(text=f'{int(textbox_amount.get())} {first_selected_opt.get()} =')
        label_result.configure(text=f'{result:.5f} {second_selected_opt.get()}')
        thirty_day_currency: List[float] = []
        sum_thirty_day = 0
        for i in range(30):
            i += 1
            old_date = datetime.datetime.now() - datetime.timedelta(i)
            previous_currency = c.get_rate(second_selected_opt.get(), first_selected_opt.get(), old_date)
            thirty_day_currency.append(float(previous_currency))
            sum_thirty_day += previous_currency
        thirty_average = sum_thirty_day / 30
        label_high_thirty.configure(text=f'{max(thirty_day_currency):.5f}')
        label_low_thirty.configure(text=f'{min(thirty_day_currency):.5f}')
        label_average_thirty.configure(text=f'{thirty_average:.5f}')
        ninety_day_currency: List[float] = []
        sum_ninety_day = 0
        for i in range(90):
            i += 1
            old_date = datetime.datetime.now() - datetime.timedelta(i)
            previous_currency = c.get_rate(second_selected_opt.get(), first_selected_opt.get(), old_date)
            ninety_day_currency.append(float(previous_currency))
            sum_ninety_day += previous_currency
        ninety_average = sum_ninety_day / 90
        label_high_ninety.configure(text=f'{max(ninety_day_currency):.5f}')
        label_low_ninety.configure(text=f'{min(ninety_day_currency):.5f}')
        label_average_ninety.configure(text=f'{ninety_average:.5f}')
    except:
        messagebox.showerror("ERROR!!!", "try again")


app = Tk()
app.option_add("*Font", "Cordia_New")
app.title("Currency Converter")
label_amount = Label(app, text="Amount", font=('', 12))
label_amount.grid(row=1, column=1, padx=20, pady=5)
textbox_amount = Entry(app, width=6)
textbox_amount.grid(row=2, column=1, padx=20, pady=5)
label_from = Label(app, text="From", font=('', 12))
label_from.grid(row=1, column=2, pady=5)
label_to = Label(app, text="To", font=('', 12))
label_to.grid(row=1, column=3, pady=5)
first_selected_opt = StringVar()
first_selected_opt.set('THB')
first_currency_opt = OptionMenu(app, first_selected_opt, *currency_list)
first_currency_opt.grid(row=2, column=2, padx=20)
second_selected_opt = StringVar()
second_selected_opt.set('USD')
second_currency_opt = OptionMenu(app, second_selected_opt, *currency_list)
second_currency_opt.grid(row=2, column=3)
cal_button = Button(app, text=">", bg='yellow')
cal_button.bind('<Button-1>', currency_converter)
cal_button.grid(row=2, column=4, padx=20)
label_first_currency = Label(app, text='')
label_first_currency.grid(row=3, columnspan=5, pady=10)
label_result = Label(app, text='', font=('', 42))
label_result.grid(row=4, columnspan=5)
label_stats = Label(app, text=f'{first_selected_opt.get()} to {second_selected_opt.get()} Stats')
label_stats.grid(row=5, column=1, padx=10, pady=5)
label_days = Label(app, text='Last 30 days', font=('', 12))
label_days.grid(row=6, column=2, padx=10, pady=5)
label_days = Label(app, text='Last 90 days', font=('', 12))
label_days.grid(row=6, column=3, padx=10, pady=5)
label_high = Label(app, text='High', font=('', 12))
label_high.grid(row=7, column=1, padx=10, pady=5)
label_low = Label(app, text='Low', font=('', 12))
label_low.grid(row=8, column=1, padx=10, pady=5)
label_average = Label(app, text='Average', font=('', 12))
label_average.grid(row=9, column=1, padx=10, pady=5)
label_high_thirty = Label(app, text='', font=('', 12))
label_high_thirty.grid(row=7, column=2, padx=10, pady=5)
label_low_thirty = Label(app, text='', font=('', 12))
label_low_thirty.grid(row=8, column=2, padx=10, pady=5)
label_average_thirty = Label(app, text='', font=('', 12))
label_average_thirty.grid(row=9, column=2, padx=10, pady=5)
label_high_ninety = Label(app, text='', font=('', 12))
label_high_ninety.grid(row=7, column=3, padx=10, pady=5)
label_low_ninety = Label(app, text='', font=('', 12))
label_low_ninety.grid(row=8, column=3, padx=10, pady=5)
label_average_ninety = Label(app, text='', font=('', 12))
label_average_ninety.grid(row=9, column=3, padx=10, pady=5)
app.mainloop()
