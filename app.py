from concurrent import futures
import logging

import uuid
import random
import grpc
import users_pb2
import users_pb2_grpc

names = ["Andres", "Simon", "Maria", "Charles"]
surnames = ["Gomez", "Lincoln", "Jenkins", "Riveros"]

class Users(users_pb2_grpc.UsersServicer):

    def GetUser(self, request, context):
        print('Hello')
        return users_pb2.GetUserResponse(user=users_pb2.User(
                id=str(uuid.uuid4()), 
                name='{0} {1}'.format(random.choice(names), random.choice(surnames)), 
                phrase='My number is {0}'.format(random.randint(1,1000))
            )
        )


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UsersServicer_to_server(Users(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
