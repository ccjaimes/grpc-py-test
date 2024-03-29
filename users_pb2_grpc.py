# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import users_pb2 as users__pb2


class UsersStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUser = channel.unary_unary(
                '/users.Users/GetUser',
                request_serializer=users__pb2.GetUserRequest.SerializeToString,
                response_deserializer=users__pb2.GetUserResponse.FromString,
                )
        self.CreateUser = channel.unary_unary(
                '/users.Users/CreateUser',
                request_serializer=users__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=users__pb2.CreateUserResponse.FromString,
                )
        self.LoginUser = channel.unary_unary(
                '/users.Users/LoginUser',
                request_serializer=users__pb2.LoginUserRequest.SerializeToString,
                response_deserializer=users__pb2.LoginUserResponse.FromString,
                )
        self.SayHello = channel.unary_unary(
                '/users.Users/SayHello',
                request_serializer=users__pb2.HelloRequest.SerializeToString,
                response_deserializer=users__pb2.HelloResponse.FromString,
                )
        self.LotsOfReplies = channel.unary_stream(
                '/users.Users/LotsOfReplies',
                request_serializer=users__pb2.HelloRequest.SerializeToString,
                response_deserializer=users__pb2.HelloResponse.FromString,
                )
        self.LotsOfGreetings = channel.stream_unary(
                '/users.Users/LotsOfGreetings',
                request_serializer=users__pb2.HelloRequest.SerializeToString,
                response_deserializer=users__pb2.DelayedHelloResponse.FromString,
                )
        self.BidiHello = channel.stream_stream(
                '/users.Users/BidiHello',
                request_serializer=users__pb2.HelloRequest.SerializeToString,
                response_deserializer=users__pb2.HelloResponse.FromString,
                )


class UsersServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoginUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LotsOfReplies(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LotsOfGreetings(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BidiHello(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UsersServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUser,
                    request_deserializer=users__pb2.GetUserRequest.FromString,
                    response_serializer=users__pb2.GetUserResponse.SerializeToString,
            ),
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=users__pb2.CreateUserRequest.FromString,
                    response_serializer=users__pb2.CreateUserResponse.SerializeToString,
            ),
            'LoginUser': grpc.unary_unary_rpc_method_handler(
                    servicer.LoginUser,
                    request_deserializer=users__pb2.LoginUserRequest.FromString,
                    response_serializer=users__pb2.LoginUserResponse.SerializeToString,
            ),
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=users__pb2.HelloRequest.FromString,
                    response_serializer=users__pb2.HelloResponse.SerializeToString,
            ),
            'LotsOfReplies': grpc.unary_stream_rpc_method_handler(
                    servicer.LotsOfReplies,
                    request_deserializer=users__pb2.HelloRequest.FromString,
                    response_serializer=users__pb2.HelloResponse.SerializeToString,
            ),
            'LotsOfGreetings': grpc.stream_unary_rpc_method_handler(
                    servicer.LotsOfGreetings,
                    request_deserializer=users__pb2.HelloRequest.FromString,
                    response_serializer=users__pb2.DelayedHelloResponse.SerializeToString,
            ),
            'BidiHello': grpc.stream_stream_rpc_method_handler(
                    servicer.BidiHello,
                    request_deserializer=users__pb2.HelloRequest.FromString,
                    response_serializer=users__pb2.HelloResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'users.Users', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Users(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/users.Users/GetUser',
            users__pb2.GetUserRequest.SerializeToString,
            users__pb2.GetUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/users.Users/CreateUser',
            users__pb2.CreateUserRequest.SerializeToString,
            users__pb2.CreateUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoginUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/users.Users/LoginUser',
            users__pb2.LoginUserRequest.SerializeToString,
            users__pb2.LoginUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/users.Users/SayHello',
            users__pb2.HelloRequest.SerializeToString,
            users__pb2.HelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LotsOfReplies(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/users.Users/LotsOfReplies',
            users__pb2.HelloRequest.SerializeToString,
            users__pb2.HelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LotsOfGreetings(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/users.Users/LotsOfGreetings',
            users__pb2.HelloRequest.SerializeToString,
            users__pb2.DelayedHelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BidiHello(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/users.Users/BidiHello',
            users__pb2.HelloRequest.SerializeToString,
            users__pb2.HelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
