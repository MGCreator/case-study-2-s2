import tkinter
import requests
from tkinter import *
from tkinter import messagebox


is_changed_value = False
is_changed_value2 = False

root = Tk()
root.title("Currency calculator")

Input = StringVar(root)
Result = StringVar(root)

Input.set("currency")
Result.set("currency")


def convertcurrency():

    try:
        clear_result()
    except:
        print("No result to clear")

    from_currency = Input.get()
    to_currency = Result.get()

    if from_currency == to_currency:
        return

    exchange_rate1 = show_rate()

    amount = float(Input_field.get())
    new_amount = float('{:.3f}'.format((amount * exchange_rate1)))

    Result_field.insert(0, str(new_amount))


def clear_all():
    Input_field.delete(0, END)
    Result_field.delete(0, END)


def clear_result():
    Result_field.delete(0, END)


def check(*args):

    if Input.get() != 'currency' and Result.get() != 'currency':
        text.set(show_rate())


Result.trace('w', check)
Input.trace('w', check)


def show_rate():
    try:
        from_currency = Input.get()
        to_currency = Result.get()
        api_key = "1Z92FHUAU5NV8Z5R"
        base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
        main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key
        req_ob = requests.get(main_url)

        result = req_ob.json()
        exchange_rate1 = float(result["Realtime Currency Exchange Rate"]['5. Exchange Rate'])
        return exchange_rate1
    except:
        tkinter.messagebox.showinfo(title=None, message="Please wait a couple of seconds and then try again.")
        return ""


if __name__ == "__main__":

    root.configure(bg='#3CAEA3')
    root.geometry("450x200")

    text = tkinter.StringVar()
    text.set('')

    head = Label(root, text="This is a real time currency calculator", fg="white", bg="#3CAEA3")
    amount_label = Label(root, text="Amount: ", fg="white", bg="#3CAEA3")
    from_currency_label = Label(root, text="From which currency?", fg="white", bg="#3CAEA3")
    to_currency_label = Label(root, text="To which currency?", fg="white", bg="#3CAEA3")
    converted_currency_label = Label(root, text="The converted amount is: ", fg="white", bg="#3CAEA3")
    rate = Label(root, textvariable=text, fg="white", bg="#3CAEA3")

    head.grid(row=0, column=1)
    amount_label.grid(row=1, column=0)
    from_currency_label.grid(row=2, column=0)
    to_currency_label.grid(row=3, column=0)
    converted_currency_label.grid(row=5, column=0)
    rate.grid(row=3, column=2)

    Input_field = Entry(root, fg="black", bg="white")
    Result_field = Entry(root, fg="black", bg="white")

    Input_field.grid(row=1, column=1, ipadx="25")
    Result_field.grid(row=5, column=1, ipadx="25")

    CurrencyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]

    fromCurrencyList = OptionMenu(root, Input, *CurrencyCode_list)
    toCurrencyList = OptionMenu(root, Result, *CurrencyCode_list)

    fromCurrencyList.config(fg="black", bg="white")
    toCurrencyList.config(fg="black", bg="white")

    fromCurrencyList.grid(row=2, column=1, ipadx=10)
    toCurrencyList.grid(row=3, column=1, ipadx=10)

    convert_button = Button(root, text="Convert", fg="white",  bg="#014421", command=convertcurrency)
    clear_button = Button(root, text="Clear", bg="light pink", command=clear_all)

    convert_button.grid(row=4, column=1)
    clear_button.grid(row=6, column=1)

    root.mainloop()

