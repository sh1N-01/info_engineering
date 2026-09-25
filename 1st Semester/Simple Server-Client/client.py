import socket
import threading

run = True

def receiveMsg(conn):
    global run
    while run:
        try:
            data = conn.recv(1024)
            if not data:
                continue
            print('Message Received: {}'.format(data.decode()))

        except socket.error as msg:
            run = False
        except KeyboardInterrupt:
            run = False

    conn.close()


def sendMessage(conn):
    global run
    while run:
        try:
            msg = input("Type Message: ")
            conn.sendall(msg.encode())
        except socket.error as err:
            run = False
        except KeyboardInterrupt:
            run = False

def start_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.50.106', 8000))
    print("Connected to the server. Type your message:")
    
    threading.Thread(target=receiveMsg, args=(s,), daemon=True).start()
    sendMessage(s)

if __name__ == "__main__":
    start_client()