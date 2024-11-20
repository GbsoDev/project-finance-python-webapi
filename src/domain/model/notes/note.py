import uuid
from uuid import UUID

from clean.sdk.domain.domain_entity import DomainEntity
from domain.model.notes import note_validator
from notes.note_type import NoteType

class Note(DomainEntity[UUID]):
    # Constructor para creación
    def __init__(self, value: float, note_type: NoteType, account_di: UUID) -> None:
        super.__init__(uuid.UUID(int=0))
        self.value = value
        self.note_type = note_type
        self.account_id = account_di
        note_validator.validate_to_create_note(self).validate_and_throw()


    # Constructor para actualizacion ORM
    def __init__(self, id: UUID, value: float, note_type: NoteType, account_di: UUID) -> None:
        super.__init__(id)
        self.value = value
        self.note_type = note_type
        self.account_id = account_di
        note_validator.validate_to_update_note(self).validate_and_throw()
