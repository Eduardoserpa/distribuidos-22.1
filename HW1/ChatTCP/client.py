import socket
import threading
from time import sleep

sock = socket.create_connection(('localhost', 10000))

print("Bate papo UOL")

user = "'/enter [username]'"
message = ""
client_online = True
def receive_server_data():
    while True:
        sleep(0.1)
        global user
        data = sock.recv(1024).decode('utf-8')
        if data:
            if "/enter " in data:
                user = data.replace('/enter ', "")
                continue
            print(data)
        else:
            break

def client_input():
    try:
        while True:
            sleep(0.5)
            global user
            global message
            global client_online
            if message != "":
                message = input()
            else:
                message = input(f"{user}: ")
                sock.sendall(message.encode('utf-8'))
                if message.lower() == "/exit":
                    client_online = False
                    break

    finally:
        print('You left the chat')
        sock.close()

thread = threading.Thread(target=receive_server_data)
thread.daemon = True
thread.start()

thread2 = threading.Thread(target=client_input)
thread2.daemon = True
thread2.start()


while client_online:
    continue
