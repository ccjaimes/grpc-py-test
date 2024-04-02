from __future__ import print_function

import logging
import hashlib
import time
import os

import grpc
import users_pb2
import users_pb2_grpc

# Codec for color output
FAILC = '\033[91m'
GOODC = '\033[92m'
ENDC = '\033[0m'

# Function to create a message stream in the client side
def get_client_stream_requests(name):
    while True:
        message = input("Input a message (or an empty message if you want to stop): ")
        if message == "":
            break

        hello_request = users_pb2.HelloRequest(greeting = message, name = name)
        yield hello_request
        time.sleep(1)

def run():
    os.system('clear')

    # Asks for a URL to connect to, or default's localhost
    ENDPOINT = str(input("Input server URL (Default: localhost)") or "localhost")
    
    with grpc.insecure_channel(f"{ENDPOINT}:50051") as channel:
        print("########### WELCOME TO GRPC CLIENT ###########")
        stub = users_pb2_grpc.UsersStub(channel)
        while True:
            print("Select an option")
            print("1. Retrieve User info")
            print("2. Create an User")
            print("3. Login with your user info")
            print("4. Say Hello")
            print("5. Say Hello and receive multiple greetings - Server Side Streaming")
            print("6. Say Hello multiple times and get a response - Client Side Streaming")
            print("7. Greet and greeted multiple times - Bidirectional Streaming")
            rpc_call = input("Which rpc would you like to make: ")

            match rpc_call:
                case "1":
                    user_request = users_pb2.GetUserRequest()
                    user_response = stub.GetUser(user_request)

                    print(f"{GOODC}Retreived user: ")
                    print(f"{user_response} {ENDC}")

                case "2":
                    name = input("Input your name: ")

                    user_request = users_pb2.CreateUserRequest(user=users_pb2.User(name=name))
                    user_response = stub.CreateUser(user_request)

                    print(f"{GOODC}Created user: ")
                    print(f"{user_response} {ENDC}")

                case "3":
                    name = input("Input your User: ")
                    pw = input("Input your Password: ")
                    pw = hashlib.md5(pw.encode()).hexdigest()

                    # In case there is no password or an incorrect one received, the server throws an error
                    try:
                        user_request = users_pb2.LoginUserRequest(name=name, pw=pw)
                        user_response = stub.LoginUser(user_request)
                        print(f"{GOODC}Logged user: ")
                        print(f"{user_response}{ENDC}")
                    except grpc.RpcError as rpc_error:
                        status = rpc_error.details()
                        print(f"{FAILC}Error: {status} {ENDC}")

                case "4":
                    name = input("Input your name: ")
                    greeting = input("Input your greeting message: ")

                    hello_request = users_pb2.HelloRequest(greeting = greeting, name = name)
                    hello_response = stub.SayHello(hello_request)

                    print(f"{GOODC}Say Hello - Response Received: ")
                    print(f"{hello_response.message}{ENDC}")

                case "5":
                    name = input("Input your name: ")
                    greeting = input("Input your greeting message: ")
                    
                    hello_request = users_pb2.HelloRequest(greeting = greeting, name = name)
                    hello_replies = stub.LotsOfReplies(hello_request)

                    print(f"{GOODC}Multiple server greetings Response Received:")
                    for hello_response in hello_replies:
                        print(f"{GOODC}{hello_response}{ENDC}")

                case "6":
                    name = input("Input your name: ")
                    delayed_response = stub.LotsOfGreetings(get_client_stream_requests(name))

                    print(f"{GOODC}Multiple client greetings Response Received:")
                    print(f"{delayed_response.message}{ENDC}")

                case "7":
                    name = input("Input your name: ")
                    print("Beginning bidirectional streaming!")
                    responses = stub.BidiHello(get_client_stream_requests(name))

                    for response in responses:
                        print(f"{GOODC}Server response Response Received: ")
                        print(f"{response}{ENDC}")

                case _:
                    break

            print("\n")

if __name__ == "__main__":
    logging.basicConfig()
    run()