import './controller_services_pb'
import './controller'

class LampController < Lamp::Service
  def initialize(sensor)
    @state = false
    @sensor = sensor


  def run
    Controller.new('Lamp', '50051', self)


  def toggle(*)
    @state = !@state
    @sensor.factor = @state
    Response.new(success: true)


  def get_state(*)
    State.new(value: @state ? 1 : 0)

