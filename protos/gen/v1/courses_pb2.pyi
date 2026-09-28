from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v1 import common_pb2 as _common_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class CreateCourseRequest(_message.Message):
    __slots__ = (
        "title",
        "max_score",
        "min_score",
        "description",
        "estimated_time",
        "preview_file_id",
        "created_by_user_id",
    )
    TITLE_FIELD_NUMBER: _ClassVar[int]
    MAX_SCORE_FIELD_NUMBER: _ClassVar[int]
    MIN_SCORE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_TIME_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    title: str
    max_score: int
    min_score: int
    description: str
    estimated_time: str
    preview_file_id: str
    created_by_user_id: str
    def __init__(
        self,
        title: _Optional[str] = ...,
        max_score: _Optional[int] = ...,
        min_score: _Optional[int] = ...,
        description: _Optional[str] = ...,
        estimated_time: _Optional[str] = ...,
        preview_file_id: _Optional[str] = ...,
        created_by_user_id: _Optional[str] = ...,
    ) -> None: ...

class UpdateCourseRequest(_message.Message):
    __slots__ = (
        "id",
        "title",
        "max_score",
        "min_score",
        "description",
        "estimated_time",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    MAX_SCORE_FIELD_NUMBER: _ClassVar[int]
    MIN_SCORE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_TIME_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    max_score: int
    min_score: int
    description: str
    estimated_time: str
    def __init__(
        self,
        id: _Optional[str] = ...,
        title: _Optional[str] = ...,
        max_score: _Optional[int] = ...,
        min_score: _Optional[int] = ...,
        description: _Optional[str] = ...,
        estimated_time: _Optional[str] = ...,
    ) -> None: ...

class GetCourseRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListCoursesRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class GetCourseResponse(_message.Message):
    __slots__ = ("course",)
    COURSE_FIELD_NUMBER: _ClassVar[int]
    course: _common_pb2.Course
    def __init__(
        self, course: _Optional[_Union[_common_pb2.Course, _Mapping]] = ...
    ) -> None: ...

class ListCoursesResponse(_message.Message):
    __slots__ = ("courses",)
    COURSES_FIELD_NUMBER: _ClassVar[int]
    courses: _containers.RepeatedCompositeFieldContainer[_common_pb2.Course]
    def __init__(
        self, courses: _Optional[_Iterable[_Union[_common_pb2.Course, _Mapping]]] = ...
    ) -> None: ...

class DeleteCourseRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
