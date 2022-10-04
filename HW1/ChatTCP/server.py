import socket
import _thread
from collections import defaultdict

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

sock.listen(5)
threads = defaultdict()
client_name_by_address = defaultdict()
client_connection_by_address = defaultdict()

default_key = "new_thread"

def send_message(message, sender=None, send_to=None):
    if message:
        if send_to:
            client_connection_by_address[send_to].sendall(message.encode('utf-8'))
        else:
            for client_address, client_connection in client_connection_by_address.items():
                if sender is not client_address and client_name_by_address.get(client_address):
                    client_connection.sendall(message.encode('utf-8'))

        print(f'sending data back to the client {message}')

def listen_client():
    print('waiting for a connection')
    connection, client_address = sock.accept()
    print(f"{client_address} connected")
    client_connection_by_address[client_address] = connection
    if len(threads.keys()) < 5:
        threads[client_address] = threads[default_key]
        threads[default_key] = _thread.start_new_thread(listen_client,())
    else:
        if client_address!=default_key:
            threads[client_address] = threads[default_key]
            del threads[default_key]
    try:
        while True:
            data = client_connection_by_address[client_address].recv(1024).decode('utf-8')
            print(f'received {data}')
            if data:
                if '/enter ' in data and not client_name_by_address.get(client_address):
                    username = data.replace('/enter ', "")
                    client_name_by_address[client_address] = username
                    send_message(data, send_to=client_address)
                    message = f"\nYou entered the chat {username}!\nPress enter to start typing"
                    send_message(message, send_to=client_address)
                    continue
                elif "/users" in data.lower():
                    message = "Users: "
                    ordered_user_list = [value for value in client_name_by_address.values()]
                    if len(ordered_user_list) > 1:
                        message += ", ".join(ordered_user_list)
                    else:
                        message += ordered_user_list[0]
                    send_message(message, send_to=client_address)
                    continue
                elif '/exit' in data.lower():
                    print('No more data from', client_address)
                    message = f"{client_name_by_address[client_address]} left the chat"
                    del client_name_by_address[client_address]
                    send_message(message, sender=client_address)
                    break

                if client_name_by_address.get(client_address):
                    message = f"{client_name_by_address[client_address]}: {data}"
                    send_message(message, sender=client_address)
                else:
                    message = "Please enter username to enter the chat"
                    send_message(message, send_to=client_address)

    finally:
        client_connection_by_address[client_address].close()

threads[default_key] = _thread.start_new_thread(listen_client,())

while True:
    continue
