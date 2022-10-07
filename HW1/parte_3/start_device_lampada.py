from _thread import *
import threading
import time

from devices.lampada import Lampada
import protobuf.gateway_pb2 as gateway_pb2

# def send_state(lampada):
#     while True:
#         time.sleep(10)
#         if lampada.ON_OFF:
#             response = gateway_pb2.DeviceResponse()
#             response.sensor_id = 1
#             response.result = f'Temperatura da sala: {lampada.temperature_sensor}'
#             lampada.socket.send(response.SerializeToString())


lampada = Lampada('228.0.0.8', 50000, 'Lampada', '127.0.0.1', 65432)
# t_1 = threading.Thread(target=send_state, args=(lampada,))
# t_1.start()
while True:
    lampada.receive_message()
