import socket
import threading

ENCODING = 'utf-8'

def recieve_msg (sock):
    while True:
        try: 
            msg = sock.recv(1024).decode(ENCODING)
            if msg == "USERNAME":
                sock.send(input("Choose a username: ").encode(ENCODING))
            else:
                print(msg)

        except:
            print ("Disconnected from Server")
            sock.close()
            break

def send_msg (sock):
    while True:
        try:
            msg = input()
            sock.send(msg.encode(ENCODING))
        except:
            break

def main ():
    host = input ("Enter sever IP (such as 127.0.0.1): ")
    port = int(input("Enter server port: "))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    threading.Thread(target=recieve_msg, args=(sock,), daemon=True).start()
    send_msg(sock)

if __name__ == "__main__":
    main()