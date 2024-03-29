from __future__ import print_function

import logging

import grpc
import users_pb2
import users_pb2_grpc


def run():
    print("Will try to greet world ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = users_pb2_grpc.UsersStub(channel)
        

        # response = stub.SayHello(users_pb2.HelloRequest(name="you"))
        response = stub.GetUser(users_pb2.GetUserRequest(id="1"))
    print("Users client received: {0}".format(response.user))


if __name__ == "__main__":
    logging.basicConfig()
    run()