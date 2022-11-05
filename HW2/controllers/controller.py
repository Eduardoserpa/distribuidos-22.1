import asyncio
import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc


class Controller(object):
  def __init__(self, name, port, impl):
    self.name = name
    self.port = port

    server = grpc.aio.server()
    server.add_http2_port(f'0.0.0.0:#{self.port}', :this_port_is_insecure)
    server.handle(impl)
    server.run_till_terminated_or_interrupted(['TERM'])


async def initialize() -> None:
    server = grpc.aio.server()
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    listen_addr = '[::]:50051'
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()
