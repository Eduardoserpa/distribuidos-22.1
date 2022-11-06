# import './controller_services_pb'
from requests import Response
from HW2.controllers.controller_pb2 import State
import controller as Controller
class FireSuppressorController():
  def __init__(self, sensor):
    self.state = False
    self.sensor = sensor
    self.sensor.fire_suppressor = self


  def run(self):
    Controller.new('FireSuppressor', '4000', self)


  def activate(self):
    self.state = True
    self.sensor.fire_suppressor_controller = True
    Response.new(success=True)


  def deactivate(self):
    self.state = False
    self.sensor.fire_suppressor_controller = False
    Response.new(success=True)


  def get_state(self):
    State.new(value=1 if self.state else 0)

