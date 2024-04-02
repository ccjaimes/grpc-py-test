from concurrent import futures
import logging

import uuid
import time
import random
import os

import grpc
import users_pb2
import users_pb2_grpc

# Names to generate and return to client
names = ["Andres", "Simon", "Maria", "Charles"]
surnames = ["Gomez", "Lincoln", "Jenkins", "Riveros"]

# Try to import value with running instance info
podId=os.environ.get('RUNNER', "far away")

# Mock hash of a password to simulate authentication
fakepw="ee959f1df4dc99154fa5898689f15fb7"

class Users(users_pb2_grpc.UsersServicer):

    # Request to get a user
    def GetUser(self, request, context):
        return users_pb2.GetUserResponse(user=users_pb2.User(
                id = str(uuid.uuid4()), 
                name = '{0} {1}'.format(random.choice(names), random.choice(surnames)), 
                phrase = 'My number is {0}'.format(random.randint(1,1000))
            )
        )

    # Request to create a user
    def CreateUser(self, request, context):
        return users_pb2.CreateUserResponse(user=users_pb2.User(
                id = str(uuid.uuid4()), 
                name = request.user.name if request.user.name != "" else '{0} {1}'.format(random.choice(names), random.choice(surnames)), 
                phrase = 'My number is {0}'.format(random.randint(1,1000))
            )
        )
    
    # Request to login with user credentials
    def LoginUser(self, request, context):
        if request.pw != fakepw:
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details("Invalid User or Password!")
            return users_pb2.LoginUserResponse()
        return users_pb2.LoginUserResponse(user=users_pb2.User(
                id = str(uuid.uuid4()),
                name = request.name if request.name != "" else '{0} {1}'.format(random.choice(names), random.choice(surnames)),
                phrase = 'My number is {0}'.format(random.randint(1,1000))
            )
        )
    
    # Request to say hello once
    def SayHello(self, request, context):
        if not request.greeting or not request.name:
            return users_pb2.HelloResponse(message="No greet identified :(")
        return users_pb2.HelloResponse(message="Greetings from {0}!".format(podId))
    
    # Request to say hello and reply multiple times
    def LotsOfReplies(self, request, context):
        if not request.greeting or not request.name:
            return users_pb2.HelloResponse(message="No greet identified :(")
        
        for i in range(5):
            yield users_pb2.HelloResponse(message="Direct Greetings No. {0} from {1}!".format(i+1, podId))
            time.sleep(2)

    # Request to send multiple hello messages with a single reply                    
    def LotsOfGreetings(self, request_iterator, context):
        delayed_rep = users_pb2.DelayedHelloResponse()
        start_t = time.time()
        msgcount = 0

        for req in request_iterator:
            msgcount += 1
            delayed_rep.request.append(req)

        end_t = int(time.time() - start_t)
        delayed_rep.message = "You sent a total of {0} messages and we took {1} seconds to process them all!".format(msgcount, end_t)
        return delayed_rep
    
    # Request to send and reply multiple hello messages
    def BidiHello(self, request_iterator, context):
        count = 0
        for req in request_iterator:
            count += 1
            yield users_pb2.HelloResponse(message="For iterated message No. {0}, Greetings from {1}".format(count, podId))

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
