import socket
import threading
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import radius

secret = "vrEGilVw@1rgMNM^$!l^t8&OkTVmXc%Hl97"
#username = "SQLAdmin"
#password = "Admin-08"
RADIUS_HOST = 'radius'
RADIUS_AUTH_PORT = 1812
r = radius.Radius(secret, RADIUS_HOST, RADIUS_AUTH_PORT)
#print('success' if r.authenticate(username, password) else 'failure')

root = Tk()
root.title("TABm")
root.geometry("500x500")
root.resizable("false", "false")

HOST = "DESKTOP-F1LAFL1"
PORT = 4780

BACKGROUND_COLOR = "#383c3c"
BACKGROUND_COLOR2 = "#303434"
BACKGROUND_COLOR3 = "#282424"
BACKGROUND_COLOR_TEXT_BOX = "#201c1c"
BACKGROUND_COLOR_BUTTONS = "#bcbcbc"
FONT = ("Calibri", 13)

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def update_message_bx(message):
    message_bx.config(state=NORMAL)
    message_bx.insert(END, message + '\n')
    message_bx.config(state=DISABLED)
    message_bx.see("end")


def log_in():
    try:
        username = username_tb.get()
        password = password_tb.get()

        if(username == "" or password == ""):
            print("Cannot be empty string")
            messagebox.showerror("Error", "Cannot be empty string")
        else:
            #enable this for RADIUS Authentication
            #if r.authenticate(username, password):
            try:
                c.connect((HOST, PORT))
                print("Successful connection to server")
                update_message_bx("Successful connection to server")
                update_message_bx("Successful login to server")
                c.sendall(bytes(username, 'utf-8'))
                writting_tb.config(state=NORMAL)
                send_btn.config(state=NORMAL)
                writting_tb.config(state=NORMAL)
                send_btn.config(state=NORMAL)
                username_tb.config(state=DISABLED)
                password_tb.config(state=DISABLED)
                join_btn.config(state=DISABLED)
                threading.Thread(target=listening_for_message, args=(c,)).start()
                send_message(c)
    
            except:
                print("Unable to establish a connection")
                messagebox.showinfo("Connection Status", "Unable to establish a connection")
                
            #else:
                #messagebox.showinfo("Try Again", "Wrong Credentials")

    except TclError as err:
        print(f"{err} has occured. Most probably username cannot be detected.")


def send_message_tk():
    send_message(c)


def send_message_with_enter(event):
    send_message(c)


root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=3)
root.grid_rowconfigure(2, weight=2)

join_frame = Frame(root, width=500, height=100, bg=BACKGROUND_COLOR)
join_frame.grid(row=0, column=0, sticky=NSEW)
#welcome = Label(join_frame, text="Welcome to our chat").pack()
messages_frame = Frame(root, width=500, height=300, bg=BACKGROUND_COLOR2)
messages_frame.grid(row=1, column=0, sticky=NSEW)
writting_frame = Frame(root, width=500, height=200, bg=BACKGROUND_COLOR3)
writting_frame.grid(row=2, column=0, sticky=NSEW)

username_lbl = Label(join_frame, text="Username", bg=BACKGROUND_COLOR, fg=BACKGROUND_COLOR_BUTTONS)
username_lbl.pack(side=LEFT, padx=10)
username_tb = Entry(join_frame, bg=BACKGROUND_COLOR_TEXT_BOX, fg='white', cursor=f"xterm {BACKGROUND_COLOR_BUTTONS}", insertbackground=BACKGROUND_COLOR_BUTTONS)
username_tb.pack(side=LEFT, padx=10)
password_lbl = Label(join_frame, text="Password", bg=BACKGROUND_COLOR, fg=BACKGROUND_COLOR_BUTTONS)
username_lbl.pack(side=LEFT, padx=10)
password_tb = Entry(join_frame, show="*", bg=BACKGROUND_COLOR_TEXT_BOX, fg='white', cursor=f"xterm {BACKGROUND_COLOR_BUTTONS}", insertbackground=BACKGROUND_COLOR_BUTTONS)
password_tb.pack(side=LEFT, padx=10)
join_btn = Button(join_frame, text="Log In", command=log_in, bg=BACKGROUND_COLOR_BUTTONS)
join_btn.pack(side=LEFT, padx=10)
#password = Label(join_frame, text="Enter password").pack(side=LEFT, padx=10)

message_bx = scrolledtext.ScrolledText(messages_frame, width=60, height=27.5, bg=BACKGROUND_COLOR2, fg="white")
message_bx.config(state=DISABLED)
message_bx.pack()

writting_tb = Entry(writting_frame, width=45, font=FONT, bg=BACKGROUND_COLOR_TEXT_BOX, fg='white', cursor=f"xterm {BACKGROUND_COLOR_BUTTONS}", insertbackground=BACKGROUND_COLOR_BUTTONS)
writting_tb.pack(side=LEFT, padx=10)
writting_tb.config(state=DISABLED)
send_btn = Button(writting_frame, text="Send", command=send_message_tk, bg=BACKGROUND_COLOR_BUTTONS)
send_btn.bind("<Return>", send_message_with_enter)
send_btn.pack(side=LEFT, padx=10)
send_btn.config(state=DISABLED)


def communicating_to_server(c):
    
    pass
    

def listening_for_message(c):

    while True:
        response = c.recv(2048).decode("utf-8")
        update_message_bx(response)

def send_message(c):

    try:
        msg = writting_tb.get()
        is_not_empty = bool(msg)
        if is_not_empty:
            c.sendall(bytes(msg, "utf-8"))
            writting_tb.delete(0, len(msg))
        else:
            pass
    except TclError as err:
        print(f"{err} has occured. Most probably username cannot be detected.")
    

def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()
            c.sendall(bytes("Close the connection:2002", "utf-8"))
            print(f"Connection with {HOST} is closed.")
root.protocol("WM_DELETE_WINDOW", on_closing)

def main():

    root.mainloop()

    communicating_to_server(c)

if __name__ == "__main__":
    main()