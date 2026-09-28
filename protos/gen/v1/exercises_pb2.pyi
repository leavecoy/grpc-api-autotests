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

class CreateExerciseRequest(_message.Message):
    __slots__ = (
        "title",
        "course_id",
        "max_score",
        "min_score",
        "order_index",
        "description",
        "estimated_time",
    )
    TITLE_FIELD_NUMBER: _ClassVar[int]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_SCORE_FIELD_NUMBER: _ClassVar[int]
    MIN_SCORE_FIELD_NUMBER: _ClassVar[int]
    ORDER_INDEX_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_TIME_FIELD_NUMBER: _ClassVar[int]
    title: str
    course_id: str
    max_score: int
    min_score: int
    order_index: int
    description: str
    estimated_time: str
    def __init__(
        self,
        title: _Optional[str] = ...,
        course_id: _Optional[str] = ...,
        max_score: _Optional[int] = ...,
        min_score: _Optional[int] = ...,
        order_index: _Optional[int] = ...,
        description: _Optional[str] = ...,
        estimated_time: _Optional[str] = ...,
    ) -> None: ...

class UpdateExerciseRequest(_message.Message):
    __slots__ = (
        "id",
        "title",
        "max_score",
        "min_score",
        "order_index",
        "description",
        "estimated_time",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    MAX_SCORE_FIELD_NUMBER: _ClassVar[int]
    MIN_SCORE_FIELD_NUMBER: _ClassVar[int]
    ORDER_INDEX_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_TIME_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    max_score: int
    min_score: int
    order_index: int
    description: str
    estimated_time: str
    def __init__(
        self,
        id: _Optional[str] = ...,
        title: _Optional[str] = ...,
        max_score: _Optional[int] = ...,
        min_score: _Optional[int] = ...,
        order_index: _Optional[int] = ...,
        description: _Optional[str] = ...,
        estimated_time: _Optional[str] = ...,
    ) -> None: ...

class GetExerciseRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListExercisesRequest(_message.Message):
    __slots__ = ("course_id",)
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    def __init__(self, course_id: _Optional[str] = ...) -> None: ...

class GetExerciseResponse(_message.Message):
    __slots__ = ("exercise",)
    EXERCISE_FIELD_NUMBER: _ClassVar[int]
    exercise: _common_pb2.Exercise
    def __init__(
        self, exercise: _Optional[_Union[_common_pb2.Exercise, _Mapping]] = ...
    ) -> None: ...

class ListExercisesResponse(_message.Message):
    __slots__ = ("exercises",)
    EXERCISES_FIELD_NUMBER: _ClassVar[int]
    exercises: _containers.RepeatedCompositeFieldContainer[_common_pb2.Exercise]
    def __init__(
        self,
        exercises: _Optional[_Iterable[_Union[_common_pb2.Exercise, _Mapping]]] = ...,
    ) -> None: ...

class DeleteExerciseRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
