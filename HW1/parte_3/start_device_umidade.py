from _thread import *
import threading
import time

from devices.umidade import Umidade
import protobuf.gateway_pb2 as gateway_pb2

def send_humidity(umidade):
    while True:
        time.sleep(10)
        if umidade.ON_OFF:
            response = gateway_pb2.DeviceResponse()
            response.sensor_id = 1
            response.result = f'Umidade da sala: {umidade.humidity_sensor}'
            umidade.socket.send(response.SerializeToString())
    

umidade = Umidade('228.0.0.8', 50000, 'Umidade', '127.0.0.1', 65432)
t_1 = threading.Thread(target=send_humidity, args=(umidade,))
t_1.start()
while True:    
    umidade.receive_message()
    if umidade.ON_OFF:
        umidade.change_humidity()
