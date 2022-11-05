import functools
import json
from querystring_parser import parser

class Server():
  HEADERS = {"Content-Type": "application/json", "Access-Control-Allow-Origin": '*'}

  def __init__(self, sensors, controllers):
    self.sensors = sensors
    self.controllers = controllers


  def call(self, env):
    symbolized_env = dict(functools.reduce(lambda output,key,value: output + [str(key), value], env))
    # env.reduce({}){|memo,(k,v)| memo[k.to_sym] = v; memo}
# lambda output, current: output + [(current, ord(current))]
    match symbolized_env:
        case { 'PATH_INFO': '/sensors', 'REQUEST_METHOD': 'GET' }:
            self.get_sensors()
        case { 'PATH_INFO': '/controllers', 'REQUEST_METHOD': 'GET' }:
            self.get_controllers()
        case { 'PATH_INFO': '/controllers', 'REQUEST_METHOD': 'POST', 'QUERY_STRING': query }:
            self.post_update_controllers(query)
        case _:
            [404, Server.HEADERS, []]


  def get_sensors(self):
    response = map(lambda sensor: json.loads({sensor.slice('name', 'state')}), self.sensors)
    return [200, Server.HEADERS, [response]]


  def get_controllers(self):
    response = \
        map(
            lambda controller: json.loads({controller.slice('name', 'state', 'kind')}),
            self.controllers
            )
    return [200, Server.HEADERS , [response]]


  def post_update_controllers(self, query):
    params = parser.parse(query)
    selected_controller = [controller for controller in self.controllers
    if controller['name'] == params['name']][0]
    if selected_controller is None:
      [404, Server.HEADERS, []]
    else:
      self.update_controller(selected_controller, params)

      [200, Server.HEADERS, []]



  def update_controller(self, controller, params):
    stub = controller['stub']
    match controller['kind']:
        case 'air_conditioner':
            temperature = State.new(value=int(params['value']))
            stub.change_temperature(temperature)
        case 'light':
            stub.toggle()
        case 'fire_suppressor':
           stub.activate() if params['value'] == 'activate' else stub.deactivate()


