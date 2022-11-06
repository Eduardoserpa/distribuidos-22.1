import logging
import grpc


class Controller(object):
  def __init__(self, name, port, impl):
    self.name = name
    self.port = port

    server = grpc.aio.server()
    server.add_http2_port(f'0.0.0.0:#{self.port}', :this_port_is_insecure)
    helloworld_pb2_grpc.add_GreeterServicer_to_server(impl(), server)
    listen_addr = f'[::]:{self.port}'
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    server.start()
    server.wait_for_termination()
