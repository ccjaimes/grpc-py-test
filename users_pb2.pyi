from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("id", "name", "phrase", "pw")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHRASE_FIELD_NUMBER: _ClassVar[int]
    PW_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    phrase: str
    pw: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., phrase: _Optional[str] = ..., pw: _Optional[str] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class CreateUserRequest(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class CreateUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class LoginUserRequest(_message.Message):
    __slots__ = ("name", "pw")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PW_FIELD_NUMBER: _ClassVar[int]
    name: str
    pw: str
    def __init__(self, name: _Optional[str] = ..., pw: _Optional[str] = ...) -> None: ...

class LoginUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class HelloRequest(_message.Message):
    __slots__ = ("name", "greeting")
    NAME_FIELD_NUMBER: _ClassVar[int]
    GREETING_FIELD_NUMBER: _ClassVar[int]
    name: str
    greeting: str
    def __init__(self, name: _Optional[str] = ..., greeting: _Optional[str] = ...) -> None: ...

class HelloResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class DelayedHelloResponse(_message.Message):
    __slots__ = ("message", "request")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    message: str
    request: _containers.RepeatedCompositeFieldContainer[HelloRequest]
    def __init__(self, message: _Optional[str] = ..., request: _Optional[_Iterable[_Union[HelloRequest, _Mapping]]] = ...) -> None: ...
