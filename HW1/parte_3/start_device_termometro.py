from _thread import *
import threading
import time

from devices.termometro import Termometro
import protobuf.gateway_pb2 as gateway_pb2

def send_temperature(termometro):
    while True:
        time.sleep(10)
        if termometro.ON_OFF:
            response = gateway_pb2.DeviceResponse()
            response.sensor_id = 1
            response.result = f'Temperatura da sala: {termometro.temperature_sensor}'
            termometro.socket.send(response.SerializeToString())
    

termometro = Termometro('228.0.0.8', 50000, 'Termometro', '127.0.0.1', 65432)
t_1 = threading.Thread(target=send_temperature, args=(termometro,))
t_1.start()
while True:
    termometro.receive_message()
