from tkinter import *

tk = Tk()
tk.geometry("300x352")
tk.resizable(0, 0)
tk.title("Simple calculator")

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def bt_clear():
    global expression
    expression = ""
    input_text.set("")

def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""


expression = ""
input_text = StringVar()

input_frame = Frame(tk, width=300, height=50, bd=0, highlightbackground="white", highlightcolor="white")
input_frame.pack()

input_field = Entry(input_frame, font=('arial', 10, 'bold'), textvariable=input_text, bg="white", width=27, bd=5)
input_field.grid(row=0, column=0)
input_field.pack()

btns_frame = Frame(tk, width=300, height=272.5, bg="grey")
btns_frame.configure(bg="white")
btns_frame.pack()

seven = Button(btns_frame, text="7", fg="black", width=13, height=3, bd=1, cursor="hand2",
               command=lambda: btn_click(7)).grid(row=0, column=0, padx=1)

eight = Button(btns_frame, text="8", fg="black", width=13, height=3, bd=1, cursor="hand2",
               command=lambda: btn_click(8)).grid(row=0, column=1, padx=1)

nine = Button(btns_frame, text="9", fg="black", width=13, height=3, bd=1, cursor="hand2",
              command=lambda: btn_click(9)).grid(row=0, column=2, padx=1)


four = Button(btns_frame, text="4", fg="black", width=13, height=3, bd=1, cursor="hand2",
              command=lambda: btn_click(4)).grid(row=1, column=0, padx=1)

five = Button(btns_frame, text="5", fg="black", width=13, height=3, bd=1, cursor="hand2",
              command=lambda: btn_click(5)).grid(row=1, column=1, padx=1)

six = Button(btns_frame, text="6", fg="black", width=13, height=3, bd=1, cursor="hand2",
             command=lambda: btn_click(6)).grid(row=1, column=2, padx=1)


one = Button(btns_frame, text="1", fg="black", width=13, height=3, bd=1, cursor="hand2",
             command=lambda: btn_click(1)).grid(row=2, column=0, padx=1)

two = Button(btns_frame, text="2", fg="black", width=13, height=3, bd=1, cursor="hand2",
             command=lambda: btn_click(2)).grid(row=2, column=1, padx=1)

three = Button(btns_frame, text="3", fg="black", width=13, height=3, bd=1, cursor="hand2",
               command=lambda: btn_click(3)).grid(row=2, column=2, padx=1)


zero = Button(btns_frame, text="0", fg="black", width=13, height=3, bd=1, cursor="hand2",
              command=lambda: btn_click(0)).grid(row=3, column=0, padx=1)

clear = Button(btns_frame, text="clear", fg="black", width=27, height=3, bd=1, cursor="hand2",
               command=lambda: bt_clear()).grid(row=3, column=1, columnspan=2, padx=1)


plus = Button(btns_frame, text="+", fg="black", width=13, height=3, bd=1, cursor="hand2",
              command=lambda: btn_click("+")).grid(row=4, column=0, padx=1)

equals = Button(btns_frame, text="=", fg="black", width=27, height=3, bd=1, cursor="hand2",
                command=lambda: bt_equal()).grid(row=4, column=1, columnspan=2 , padx=1)


minus = Button(btns_frame, text="-", fg="black", width=13, height=3, bd=1, cursor="hand2",
               command=lambda: btn_click("-")).grid(row=5, column=0, padx=1)

multiply = Button(btns_frame, text="*", fg="black", width=13, height=3, bd=1, cursor="hand2",
                  command=lambda: btn_click("*")).grid(row=5, column=1, padx=1)

divide = Button(btns_frame, text="/", fg="black", width=13, height=3, bd=1, cursor="hand2",
                command=lambda: btn_click("/")).grid(row=5, column=2, padx=1)

tk.mainloop()
