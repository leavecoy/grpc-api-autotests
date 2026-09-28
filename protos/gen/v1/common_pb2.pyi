from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class User(_message.Message):
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

class File(_message.Message):
    __slots__ = ("id", "filename", "directory", "url")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    filename: str
    directory: str
    url: str
    def __init__(
        self,
        id: _Optional[str] = ...,
        filename: _Optional[str] = ...,
        directory: _Optional[str] = ...,
        url: _Optional[str] = ...,
    ) -> None: ...

class Course(_message.Message):
    __slots__ = (
        "id",
        "title",
        "max_score",
        "min_score",
        "description",
        "preview_file",
        "estimated_time",
        "created_by_user",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    MAX_SCORE_FIELD_NUMBER: _ClassVar[int]
    MIN_SCORE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FILE_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    max_score: int
    min_score: int
    description: str
    preview_file: File
    estimated_time: str
    created_by_user: User
    def __init__(
        self,
        id: _Optional[str] = ...,
        title: _Optional[str] = ...,
        max_score: _Optional[int] = ...,
        min_score: _Optional[int] = ...,
        description: _Optional[str] = ...,
        preview_file: _Optional[_Union[File, _Mapping]] = ...,
        estimated_time: _Optional[str] = ...,
        created_by_user: _Optional[_Union[User, _Mapping]] = ...,
    ) -> None: ...

class Exercise(_message.Message):
    __slots__ = (
        "id",
        "title",
        "course_id",
        "max_score",
        "min_score",
        "order_index",
        "description",
        "estimated_time",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_SCORE_FIELD_NUMBER: _ClassVar[int]
    MIN_SCORE_FIELD_NUMBER: _ClassVar[int]
    ORDER_INDEX_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_TIME_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    course_id: str
    max_score: int
    min_score: int
    order_index: int
    description: str
    estimated_time: str
    def __init__(
        self,
        id: _Optional[str] = ...,
        title: _Optional[str] = ...,
        course_id: _Optional[str] = ...,
        max_score: _Optional[int] = ...,
        min_score: _Optional[int] = ...,
        order_index: _Optional[int] = ...,
        description: _Optional[str] = ...,
        estimated_time: _Optional[str] = ...,
    ) -> None: ...

class Token(_message.Message):
    __slots__ = ("token_type", "access_token", "refresh_token")
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    token_type: str
    access_token: str
    refresh_token: str
    def __init__(
        self,
        token_type: _Optional[str] = ...,
        access_token: _Optional[str] = ...,
        refresh_token: _Optional[str] = ...,
    ) -> None: ...
