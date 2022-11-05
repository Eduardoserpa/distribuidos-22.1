# frozen_string_literal: true

import random
import time
import pika

class TemperatureSensor():
#   attr_writer :factor
#   attr_reader :state

  def __init__(self):
    self.state = 0
    self.factor = 0


  def run(self):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    self.channel = connection.channel()

    self.queue = self.channel.queue_declare(queue='temperature_sensor')
    # connection.start

    while(True):
      self.update_state
      self.s_state
      time.sleep(3)


    connection.close()


  def s_state(self):
    # self.channel.default_exchange.publish(self.state.to_s, routing_key=self.queue.name)
    self.channel.basic_publish(str(self.state), routing_key=self.queue.name)


  def update_state(self):
    self.state = self.factor + random.randint(-3, 3)
    print(self.state)

