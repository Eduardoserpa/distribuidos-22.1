import './actuators/tv_controller'
import fire_suppressor_sensor

  class FireSuppressor:
    def __init__(self):
      self.sensor = fire_suppressor_sensor()
      self.actuator = FireSuppressorController.new(self.sensor)

      t1 = Thread.new do
        self.actuator.run


      t2 = Thread.new do
        self.sensor.run


      t1.join
      t2.join
    rescue Interrupt
      print('Closing...')


Devices::FireSystem.new
