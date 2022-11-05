import './controller_services_pb'
import controller as Controller

class AirConditionerController < AirConditioner::Service
  def initialize(self,sensor):
    self.state = 0
    self.sensor = sensor


  def run(self):
    Controller.new('AirConditioner', '50052', self)


  def change_temperature(self, temperature):
    self.state = temperature.value
    self.sensor.factor = temperature.value
    Response.new(success: true)


  def get_state(self):
    State.new(value: self.state)
