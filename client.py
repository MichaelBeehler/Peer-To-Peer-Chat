import socket
import threading
from datetime import datetime

ENCODING = 'utf-8'

def recieve_msg (sock):
    while True:
        try: 
            msg = sock.recv(1024).decode(ENCODING)
            if not msg:
                print ("User has left the chat.")
                break
            
            timeStamp = datetime.now().strftime("[%H:%M:%S]")
            print(f"{timeStamp} {msg}")

        except:
            break


def send_msg (sock):
    while True:
        try:
            msg = input()

            if msg.startswith("/"):

                if msg.strip() == "/exit":

                    print("Exiting chat...")
                    sock.close()
                    break

                else:
                    print("Unknown command. Type /exit to quit.")

            else:
                sock.send(msg.encode(ENCODING))
                timeStamp = datetime.now().strftime("[%H:%M:%S]")
                print(f"{timeStamp} You: {msg}")
        except:
            break

def main ():
    host = input ("Enter sever IP (such as 127.0.0.1): ")
    port = int(input("Enter server port: "))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    msg = sock.recv(1024).decode(ENCODING)

    if msg == "USERNAME":
        username = input("Enter your Username: ")
        sock.send(username.encode(ENCODING))

    threading.Thread(target=recieve_msg, args=(sock,), daemon=True).start()
    send_msg(sock)

if __name__ == "__main__":
    main()