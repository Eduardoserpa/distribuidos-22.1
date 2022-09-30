## Again we import the necessary socket python module
import socket
import re
from functools import reduce

## Here we define the UDP IP address as well as the port number that we have
## already defined in the client python script.
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789

## declare our serverSocket upon which
## we will be listening for UDP messages
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
## One difference is that we will have to bind our declared IP address
## and port number to our newly declared serverSock
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

while True:
    data, addr = serverSock.recvfrom(1024)
    msg = data.decode('utf-8')
    result = "Operation not valid"
    if msg == "exit":
        result = "Goodbye, cruel world"
        print("Message: ", result)
        break
    math_operators = ["+", "-", "*", "/"]
    valid_operation = False
    for operator in math_operators:
        if operator in msg:
            valid_operation = True

    if not valid_operation:
        serverSock.sendto(str(result).encode('utf-8'), addr)
        print("Server sent : ", result)
        continue

    numbers = [float(s) for s in re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", msg)]
    if "*" in msg:
        result = reduce(lambda a, b: a * b, numbers)
    if "/" in msg:
        result = reduce(lambda a, b: a / b, numbers)
    if "+" or "-" in msg:
        result = reduce(lambda a, b: a + b, numbers)

    serverSock.sendto(str(result).encode('utf-8'), addr)
    print("Server sent : ", result)
