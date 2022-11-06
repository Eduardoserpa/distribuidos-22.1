from sre_parse import State
from requests import Response
import controller as Controller

class AirConditionerController():
  def initialize(self,sensor):
    self.state = 0
    self.sensor = sensor


  def run(self):
    Controller('AirConditioner', '50052', self)


  def change_temperature(self, temperature):
    self.state = temperature.value
    self.sensor.factor = temperature.value
    Response.new(success=True)


  def get_state(self):
    State.new(value=self.state)
