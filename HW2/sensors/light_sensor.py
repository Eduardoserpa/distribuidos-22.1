# frozen_string_literal: true

import random
import time
import pika

class LightSensor(object):
#   attr_writer :factor
#   attr_reader :state

  def __init__(self):
    self.state = 0
    self.factor = False

  def run(self):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    self.channel = connection.channel()

    self.queue = self.channel.queue_declare(queue='light_sensor')

    while(True):
      self.update_state()
      self.s_state()
      time.sleep(10)


    connection.close()


  def s_state(self):
    self.channel.basic_publish(str(self.state), routing_key=self.queue.name)


  def update_state(self):
    self.state = random.randint(80, 100) if self.factor else random.randint(0, 20)
    print(self.state)

