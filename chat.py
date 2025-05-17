import socket
import threading

BUFFERSIZE = 1024
ENCODING = 'utf-8'

def recieve_messages(conn): 
    while True:
        try:
            message = conn.recv(BUFFERSIZE).decode(ENCODING)
            if message: 
                print(f"\nAnonymous: {message}")
            else:
                break
        except:
            break

def send_message (conn):
    while True:
        message = input()
        try:
            conn.send(message.encode(ENCODING))
        except:
            print("Connection Closed!")
            break

def start_chat ():
    print("Welcome to chat!")
    mode = input ("Would you like to host (h) or join (j) this chat?").strip().lower()

    if mode == 'h':
        host = '0.0.0.0'
        port = int(input("Enter port to host on: "))
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(1)
        print (f"Waiting for connection on port {port}...")
        conn, addr = server.accept()
        print(f"Connected by {addr[0]}:{addr[1]}")

    elif mode == 'j':
        host = input("Enter the host IP to connect to: ").strip()
        port = int(input("Enter the port to connect to: "))
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((host, port))
        print (f"Connected to {host}:{port}")

    else:
        print ("Invalid mode. Use 'h' to host or 'j' to join.")
        return 
    
    threading.Thread(target=recieve_messages, args=(conn, ), daemon=True).start()
    send_message(conn)

if __name__ == "__main__":
    start_chat()