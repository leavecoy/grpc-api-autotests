from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v1 import common_pb2 as _common_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class CreateUserRequest(_message.Message):
    __slots__ = ("email", "password", "last_name", "first_name", "middle_name")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    MIDDLE_NAME_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    last_name: str
    first_name: str
    middle_name: str
    def __init__(
        self,
        email: _Optional[str] = ...,
        password: _Optional[str] = ...,
        last_name: _Optional[str] = ...,
        first_name: _Optional[str] = ...,
        middle_name: _Optional[str] = ...,
    ) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ("id", "email", "last_name", "first_name", "middle_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    MIDDLE_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    email: str
    last_name: str
    first_name: str
    middle_name: str
    def __init__(
        self,
        id: _Optional[str] = ...,
        email: _Optional[str] = ...,
        last_name: _Optional[str] = ...,
        first_name: _Optional[str] = ...,
        middle_name: _Optional[str] = ...,
    ) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _common_pb2.User
    def __init__(
        self, user: _Optional[_Union[_common_pb2.User, _Mapping]] = ...
    ) -> None: ...
