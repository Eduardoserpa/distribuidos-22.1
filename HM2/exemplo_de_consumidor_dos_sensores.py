import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel1 = connection.channel()
    channel2 = connection.channel()
    channel3 = connection.channel()

    channel1.queue_declare(queue='Temperatura')
    channel2.queue_declare(queue='Umidade')
    channel3.queue_declare(queue='Luminosidade')


    def callback1(ch, method, properties, body):
        print(" [x] Temperatuda %r" % body)

    def callback2(ch, method, properties, body):
        print(" [x] Umidade %r" % body)

    def callback3(ch, method, properties, body):
        print(" [x] Luminosidade %r" % body)

    channel1.basic_consume(queue='Temperatura', on_message_callback=callback1, auto_ack=True)
    channel2.basic_consume(queue='Umidade', on_message_callback=callback2, auto_ack=True)
    channel3.basic_consume(queue='Luminosidade', on_message_callback=callback3, auto_ack=True)


    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel1.start_consuming()
    channel2.start_consuming()
    channel3.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)