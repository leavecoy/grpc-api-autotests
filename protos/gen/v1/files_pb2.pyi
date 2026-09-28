from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v1 import common_pb2 as _common_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileRequest(_message.Message):
    __slots__ = ("filename", "directory", "content")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    filename: str
    directory: str
    content: bytes
    def __init__(
        self,
        filename: _Optional[str] = ...,
        directory: _Optional[str] = ...,
        content: _Optional[bytes] = ...,
    ) -> None: ...

class GetFileRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetFileResponse(_message.Message):
    __slots__ = ("file",)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: _common_pb2.File
    def __init__(
        self, file: _Optional[_Union[_common_pb2.File, _Mapping]] = ...
    ) -> None: ...

class DeleteFileRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
