import pika
import random
import time


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel1 = connection.channel()
channel2 = connection.channel()
channel3 = connection.channel()



channel1.queue_declare(queue='Temperatura')
channel2.queue_declare(queue='Umidade')
channel3.queue_declare(queue='Luminosidade')


temp = random.randint(0,50)
umd = random.randint(20,70)
lumino = random.randint(20,70)

while(True):
    print('Temp:' + str(temp))
    print('Umidade:' + str(umd))
    print('Lumin:' + str(lumino))

    channel1.basic_publish(exchange='', routing_key='Temperatura', body=str(temp))
    channel2.basic_publish(exchange='', routing_key='Umidade', body=str(umd))
    channel3.basic_publish(exchange='', routing_key='Luminosidade', body=str(lumino))
    temp = random.randint(temp-2, temp+2)
    umd = random.randint(umd-2, umd+2)
    lumino = random.randint(lumino-2, lumino+2)
    time.sleep(10)

connection.close()