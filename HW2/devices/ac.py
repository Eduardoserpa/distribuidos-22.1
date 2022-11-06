import threading
from HW2.controllers.ac_controller import AirConditionerController
from HW2.sensors.temperature_sensor import TemperatureSensor

class AirConditioner:
  def __init__(self):
    self.sensor = TemperatureSensor()
    self.controller = AirConditionerController(self.sensor)

    try:
      t1 = threading.Thread(target=self.controller.run)
      t2 = threading.Thread(target=self.sensor.run)

      t1.join()
      t2.join()

    except ValueError:
      print('Closing...')
