from uuid import UUID
import uuid
from clean.sdk.domain.domain_entity import DomainEntity
from notes.note import Note


class Account(DomainEntity[UUID]):
    def __init__(self, description) -> None:
        super.__init__(uuid.UUID(int=0))
        self.__description = description
        self.__notes: list[Note] = []

    @property
    def description(self) -> str:
        return self.__description

    @property
    def notes(self) -> list[Note]:
        return self.__notes
