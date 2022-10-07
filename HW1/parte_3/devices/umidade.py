from devices.base import BaseDevice
import protobuf.gateway_pb2 as gateway_pb2

class Umidade(BaseDevice):
    def __init__(self,ip_multicast,port_multicast,
                       Nome_Dispositivo,server_ip,server_port):
        super().__init__(ip_multicast,port_multicast,
                       Nome_Dispositivo,server_ip,server_port)
        
        self.humidity_set = 40
        self.humidity_sensor = 35
    
    # def change_temperature(self):
    def change_humidity(self):
        if self.humidity_sensor>self.humidity_set:
            self.humidity_sensor = self.humidity_sensor-1
        
        if self.humidity_sensor<self.humidity_set:
            self.humidity_sensor = self.humidity_sensor+1
    
    def receive_message(self):
        response = gateway_pb2.DeviceResponse()
        request = gateway_pb2.GatewayRequest()
        request.ParseFromString(self.socket.recv(1024))
        
        if self.IsOn():
            if request.request_type == 2:
                if request.aux =='umid':
                    self.humidity_set = float(request.value)
                    response.result =f'Umidade escolhida: {self.humidity_set}'
                    
            # if request.request_type == 0:
            #     if request.aux =='ssumid':
            #         response.result =f'Setted Humidity:{self.humidity_set}'
        
            if request.request_type == 1:
                response.result = f'Umidade da sala: {self.humidity_sensor}'
        
            if request.request_type == 3:
                self.ON_OFF=False
                response.result =f'{self.nome} Dispositivo: OFF'
                
            if request.request_type == 4:
                # response.result = '\n Modifique Umidade: Digite umid \n Modifique Umidade: Digite ssumid \n Veja Umidade da sala: Digite sensor \n Desligue o Umidificador: Digite off'
                # response.object_commands[:] =['umid','ssumid','sensor','off']
                response.result = '\n Modifique Umidade: Digite umid \n Veja Umidade da sala: Digite sensor \n Desligue o Umidificador: Digite off'
                response.object_commands[:] =['umid','sensor','off']
        else:
            response.result=f'{self.nome} em standby, para usar digite on'
            response.object_commands[:] =['on']
            if request.request_type == 3:
                self.ON_OFF=True
                response.result =f'{self.nome} Dispositivo: ON'
        
        response.name = self.nome
        response.object_status = self.ON_OFF
        response.sensor_id = 0
        response.client_id=request.client_id
        
        self.socket.send(response.SerializeToString())
