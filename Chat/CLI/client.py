import socket
import threading

HOST = "127.0.0.1"
PORT = 4780

def communicating_to_server(c):
    username = input("Username: ")
    is_not_empty = bool(username)
    while(not is_not_empty):
        username = input("Username: ")
        is_not_empty = bool(username)

    c.sendall(bytes(username, 'utf-8'))
    threading.Thread(target=listening_for_message, args=(c,)).start()
    send_message(c)

def listening_for_message(c):

    while True:
        response = c.recv(2048).decode("utf-8")
        print(response)

def send_message(c):

    while True:
        msg = input("Message: ")
        is_not_empty = bool(msg)
        if is_not_empty:
            c.sendall(bytes(msg, "utf-8"))
        else:
            pass



def main():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        c.connect((HOST, PORT))
        print("Successful connection to server")
        communicating_to_server(c)
    except:
        print("Unable to establish a connection")

if __name__ == "__main__":
    main()