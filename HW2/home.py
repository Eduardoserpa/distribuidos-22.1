import threading
import time
import pika
class Home():
  def __init__(self):
    self.sensors = []
    self.controllers = []
    sensors_thread =  threading.Thread(target=self.start_sensors_comms)
    controller_thread = threading.Thread(target=self.start_controllers_comms)
    webserver_thread = threading.Thread(target=self.start_webserver)

    sensors_thread.join
    controller_thread.join
    webserver_thread.join
    self.sensors_connection.close()

    exit(0)


  def start_sensors_comms(self):
    self.sensors_connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    self.sensors_connection.start

    channel = self.sensors_connection.create_channel
    self.sensors.push([
      { 'name': 'light.sensor1' },
      { 'name': 'temperature.sensor1' },
      { 'name': 'smoke.sensor1' }
    ])

    for sensor in self.sensors:
      sensor['queue'] = channel.queue(sensor['name'])

      # sensor['queue'].subscribe do |_, _, body|
      #   sensor['state'] = body
      #   sensor['last_update'] = time.now()



    while(True):
      for sensor in self.sensors:
        if sensor['last_update'] is None:
          next

        last_update_diff = time.localtime() - sensor['last_update']
        if last_update_diff > 3:
          sensor['state'] = None

      time.sleep(5)



  def start_controllers_comms(self):
    self.controllers.append([
      {
        'name': 'Ar Condicionado 1',
        'stub': AirConditioner::Stub.new('localhost:50052', :this_channel_is_insecure),
        'kind': 'air_conditioner'
      },
      {
        'name': 'Sistema contra incêndio',
        'stub': FireSprinkler::Stub.new('localhost:4000', :this_channel_is_insecure),
        'kind': 'fire_suppressor'
      },
      {
        'name': 'Lâmpada',
        'stub': Lamp::Stub.new('localhost:50051', :this_channel_is_insecure),
        'kind': 'light'
      }
    ])

    while(True):
      for controller in self.controllers:
        try:
          state = controller['stub'].get_state()
          match controller['kind']:
            case 'air_conditioner':
              controller[:state] = state.value
            case 'light':
              controller[:state] = state.value == 1
            case 'fire_suppressor':
              controller[:state] = state.value == 1

        except ValueError:
          controller['state'] = None

      time.sleep(1)



  def start_webserver(self):
    Rack::Handler::WEBrick.run(WebServer.new(self.sensors, self.controllers), :Port => 9292)

Home()
