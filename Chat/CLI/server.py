import socket
import threading

PORT = 4780
NUM_OF_NODES = 5

connections = []

def send_to_all(message):
    #add timestamps
    for conn in connections:

        send_to_a_client(conn[2], message)

def send_to_a_client(c, message):

    #c.sendall(bytes(message, "utf-8"))
    c.sendall(message.encode())

def handling_clients(c, addr):
    
    while True:
        name = c.recv(2048).decode("utf-8")
        is_not_empty = bool(name)
        if is_not_empty:
            connections.append((addr[0], name, c))
            print(f"{name} has entered the chat")
            join_msg = f"{name} has entered the chat"
            send_to_all(join_msg)
            c.sendall(bytes("\nWelcome to the Multiverse", "utf-8"))
            
            print(connections)
            break
        else:
            print("Invalid name (Empty string)")
            send_to_a_client(c, "Cannot be empty string")

    threading.Thread(target = listening_for_message, args = (c,name)).start()

def listening_for_message(c, username):
    while True:
        response = c.recv(2048).decode("utf-8")
        is_not_empty = bool(response)
        if is_not_empty:
            msg = f"<{username}>{response}"
            send_to_all(msg)
        else:
            print(f"Empty message from {username}")
    

def disconnecting_clients(c, addr):
    connections.remove(c)


def main():
    #                 Using IPv4      Using TCP protocol
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Server socket is created")

    try:
        #s.bind(('localhost', PORT))
        s.bind(('localhost', PORT))
        print(f"Server is running localy on port {PORT}")
        print("Waiting for connection...")
    except:
        print("Unable to connect to host")

    s.listen(NUM_OF_NODES)
    
    while True:
        c, addr = s.accept()
        threading.Thread(target = handling_clients, args = (c,addr)).start()

if __name__ == "__main__":
    main()
    
