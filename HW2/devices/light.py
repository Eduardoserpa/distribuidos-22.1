import threading
from HW2.controllers.light_controller import LightController
from HW2.sensors.light_sensor import LightSensor
class Light:
  def __init__(self):

    self.sensor = LightSensor
    self.controller = LightController(self.sensor)
    try:
      t1 = threading.Thread(self.controller.run)
      t2 = threading.Thread(self.sensor.run)

      t1.join()
      t2.join()

    except ValueError:
      print('Closing...')


