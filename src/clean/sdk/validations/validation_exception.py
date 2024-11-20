from validation_set import ValidationSet


class ValidationException(Exception):
    def __init__(self, validation_set: ValidationSet) -> None:
        super().__init__(validation_set.__error_message)
        self.__message = validation_set.__error_message
        self.__validation_set = validation_set

    @property
    def message(self) -> str:
        return self.__message

    @property
    def validation_set(self) -> str:
        return self.__validation_set
