# frozen_string_literal: true

import random
import time
import pika

class FireSuppressorSensor(object):
  def __init__(self):
    self.smoke_sensor = 0.0
    self.fire_suppressor_controller = False


  def run(self):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    self.channel = connection.channel()

    self.queue = self.channel.queue_declare(queue='smoke_sensor')

    while(True):
      self.update_state()
      self.s_state()
      time.sleep(3)


    connection.close()


  def s_state(self):
    # self.channel.default_exchange.publish(self.smoke_sensor.to_s, routing_key=self.queue.name)
    self.channel.basic_publish(str(self.smoke_sensor), routing_key=self.queue.name)


  def update_state(self):
    self.smoke_sensor = \
    random.randint(0, 10) if self.fire_suppressor_controller else random.randint(0,100)
    print(self.smoke_sensor)

    if self.smoke_sensor >= 80:
      self.fire_suppressor.activate()
    else:
      self.fire_suppressor.deactivate()


