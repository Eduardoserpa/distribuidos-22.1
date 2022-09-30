## Again we import the necessary socket python module
import socket
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

while True:
    msg = input("Enter your value: ")
    s.sendto(str.encode(msg), (UDP_IP_ADDRESS, UDP_PORT_NO))
    if msg == "exit":
        break
    data, address = s.recvfrom(4096)
    print("Client received : ", data.decode('utf-8'))
s.close()
