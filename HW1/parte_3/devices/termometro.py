from devices.base import BaseDevice
import protobuf.gateway_pb2 as gateway_pb2

class Termometro(BaseDevice):
    def __init__(self,ip_multicast,port_multicast,
                       Nome_Dispositivo,server_ip,server_port):
        super().__init__(ip_multicast,port_multicast,
                       Nome_Dispositivo,server_ip,server_port)
        
        self.temperature_set = 20
        self.temperature_sensor = 25
    
    def change_temperature(self):
        if self.temperature_sensor>self.temperature_set:
            self.temperature_sensor = self.temperature_sensor-0.1
        
        if self.temperature_sensor<self.temperature_set:
            self.temperature_sensor = self.temperature_sensor+0.1
    
    def receive_message(self):
        response = gateway_pb2.DeviceResponse()
        request = gateway_pb2.GatewayRequest()
        request.ParseFromString(self.socket.recv(1024))
        
        if self.IsOn():
            # if request.request_type == 2:
            #     if request.aux =='temp':
            #         self.temperature_set = float(request.value)
            #         response.result =f'Setted Temperature: {self.temperature_set}'
                    
            # if request.request_type == 0:
            #     if request.aux =='sstemp':
            #         response.result =f'Setted Temperature:{self.temperature_set}'
        
            if request.request_type==1:
                response.result = f'Temperatura da Sala: {self.temperature_sensor}'
        
            if request.request_type == 3:
                self.ON_OFF=False
                response.result =f'{self.nome} Dispositivo: OFF'
                
            if request.request_type == 4:
                # response.result = '\n Modifique Temperatura: Digite temp \n Modifique Temperatura: Digite sstemp \n Veja Temperatura da sala: Digite sensor \n Desligue o Ar: Digite off'
                # response.object_commands[:] =['temp','sstemp','sensor','off']
                response.result = '\n Veja Temperatura da sala: Digite sensor \n Desligue o Termômetro: Digite off'
                response.object_commands[:] =['sensor','off']
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
