from rich.console import Console
from rich.table import Table

from HW2.controllers.controller_pb2 import State

class Client():
  def __init__(self, sensors, controllers):
    # self.prompt = TTY::Prompt.new
    self.prompt = Console()
    self.sensors = sensors
    self.controllers = controllers

    self.listen_commands()


  def listen_commands(self):
    while True:
      key = self.prompt.input() # blocking
      if key is None:
        self.output()
      else:
        self.request_update_controller()




  def output(self):
    rows = map(lambda sensor: [sensor['name'], sensor['value']], self.sensors)
    # table = TTY::Table.new(['Dispositivo', 'Estado'], rows).rer(:unicode, alignments: %i[left center])
    table = Table(['Dispositivo', 'Estado'], rows).rer('unicode', alignments=%i[left center])
    self.prompt.print("\e[H\e[2J#{table}\nPressione qualquer tecla para alterar um atuador.")


  def request_update_controller(self):
    # name = self.prompt.select('Selecione um atuador:', self.controllers.map { |act| act[:name] })
    name = self.prompt.input('Selecione um atuador:', map(lambda controller: controller['name'], self.controllers))
    selected_controller = [act for act in self.controllers if act['name'] == name][0]
    stub = selected_controller['stub']

    match selected_controller['kind']:
        case 'air_conditioner':
            state = self.prompt.ask('Qual valor deseja?')
            temperature = State.new(value=int(state))
            stub.change_temperature(temperature)
        case 'light':
            stub.toggle()
        case 'fire_sprinkler':
            fire_sprinker_options = {'Ativar': True, 'Desativar': False}

            enable = self.prompt.select('Deseja ativar ou desativar?', fire_sprinker_options)

            stub.activate() if enable else stub.deactivate()




