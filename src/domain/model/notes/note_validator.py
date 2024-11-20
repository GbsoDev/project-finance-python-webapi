from clean.sdk.validations.validation_set import ValidationSet
from notes import note_parameters
from note_type import NoteType
from resources import validation_error_messages
from notes.note import Note


def validate_to_create_note(note: Note) -> ValidationSet:
    validationset = ValidationSet(
        validation_error_messages.INVALID_PARAMETERS_FOR_CREATING_THE_ENTITY)
    {
        validationset
        .add_is_not_none_validation(note.value, validation_error_messages.ERROR_NONE_PARAMETER, "value")
        .add_is_not_empty_validation(note.value, validation_error_messages.ERROR_EMPTY_PARAMETER, "value")
        .add_greater_than_or_equal_to_validation(note.value, note_parameters.MIN_VALUE, validation_error_messages.ERROR_GREATER_THAN_OR_EQUAL_PARAMETER, "value", note_parameters.MIN_VALUE)

        .add_is_not_none_validation(note.note_type, validation_error_messages.ERROR_NONE_PARAMETER, "note_type")
        .add_is_not_empty_validation(note.note_type, validation_error_messages.ERROR_EMPTY_PARAMETER, "note_type")
        .add_is_defined_validation(note.note_type, validation_error_messages.ERROR_UNDEFINED_VALUE_FOR_ENUM, note.note_type, type(NoteType).__name__)

        .add_is_not_none_validation(note.account_id, validation_error_messages.ERROR_NONE_PARAMETER, "account_id")
        .add_is_not_empty_validation(note.account_id, validation_error_messages.ERROR_EMPTY_PARAMETER, "account_id")
    }


def validate_to_update_note(note: Note) -> ValidationSet:
    validationset = validate_to_create_note(note)
    validationset.set_error_message(
        validation_error_messages.INVALID_PARAMETERS_FOR_UPDATING_THE_ENTITY)
    {
        validationset
        .add_is_not_none_validation(note.id, validation_error_messages.ERROR_NONE_PARAMETER, "id")
        .add_is_not_empty_validation(note.id, validation_error_messages.ERROR_EMPTY_PARAMETER, "id")
    }
