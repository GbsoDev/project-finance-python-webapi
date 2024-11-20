from typing import Generic, TypeVar
from uuid import UUID

TId = TypeVar('TId', str, int, UUID)


class DomainEntity(Generic[TId]):
    def __init__(self, id: TId) -> None:
        self.__id = id

    @property
    def id(self) -> TId:
        return self.__id
