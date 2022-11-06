from HW2.controllers.controller import Controller
from requests import Response

from HW2.controllers.controller_pb2 import State

class LightController():
  def __init__(self,sensor):
    self.state = False
    self.sensor = sensor


  def run(self):
    Controller.new('Light', '50051', self)


  def toggle(self):
    self.state = not self.state
    self.sensor.factor = self.state
    Response.new(success=True)


  def get_state(self):
    State.new(value=1 if self.state else 0)

