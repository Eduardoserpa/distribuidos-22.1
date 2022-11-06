import threading
from HW2.controllers.fire_suppressor_controller import FireSuppressorController
from HW2.sensors.fire_suppressor_sensor import FireSuppressorSensor

class FireSuppressor:
  def __init__(self):
    self.sensor = FireSuppressorSensor()
    self.controller = FireSuppressorController(self.sensor)
    try:
      t1 = threading.Thread(target=self.controller.run)
      t2 = threading.Thread(target=self.sensor.run)

      t1.join()
      t2.join()

    except ValueError:
      print('Closing...')
