import threading
import socket

HOST = '0.0.0.0'
PORT = 5555
ENCODING = 'utf-8'
clients = {}

def broadcast (message, senderConn=None):
    for conn in clients:
        if conn != senderConn:
            try:
                conn.send(message.encode(ENCODING))
            except:
                conn.close()
                del clients[conn]


def handle_client (conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send("USERNAME".encode(ENCODING))
    username = conn.recv(1024).decode(ENCODING)
    clients[conn] = username
    broadcast(f"{username} has entered the chat!")

    while True:
        try:
            msg = conn.recv(1024).decode(ENCODING)
            if msg:
                broadcast(f"{username}: {msg}", senderConn=conn)
            else:
                break
        except:
            break

    conn.close()
    broadcast(f"{username} has left the chat!")
    del clients[conn]

def start ():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[SERVER STARTED] Listening on port {PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
        thread.start()

if __name__ == "__main__":
    start()