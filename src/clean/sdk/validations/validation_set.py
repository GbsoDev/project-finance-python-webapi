from enum import Enum
from typing import Callable, List, Optional, TypeVar
from . import *
from validation_error import ValidationError
from validation_exception import ValidationException
from validation_set import ValidationSet

T = TypeVar('T')
TEnum = TypeVar('TEnum', bound=Enum)


class ValidationSet:
    def __init__(self, error_message: Optional[str] = None) -> None:
        self.__error_message = error_message
        self.__errors: List[ValidationError] = []

    def add_error(self, message) -> None:
        self.__errors.append(ValidationError(message))

    def validate_and_throw(self) -> None:
        if not self.is_valid:
            raise ValidationException(self)

    def set_error_message(self, error_message: Optional[str]) -> ValidationSet:
        self.__error_message = error_message
        return self

    @property
    def is_valid(self):
        return not any(self.__errors)

    @property
    def __error_message(self) -> str:
        return self.__error_message

    @property
    def __errors(self) -> str:
        return self.__errors

    def add_greater_than_validation(self, value: T, min: T, message_resource: str, *message_params):
        """
        Checks if the value is greater than the specified start value and adds an error message if it is not.
        
        Args:
            validation_set: The ValidationSet instance to add the validation to.
            value: The value to validate.
            start: The start value to compare against.
            message_resource: The resource string for the error message.
            message_params: The parameters to format the message.
        
        Returns:
            The updated ValidationSet instance.
        """
        return self.add_validation(self, is_greater_than(value, min), message_resource, *message_params)

    def add_greater_than_or_equal_to_validation(self, value: T, min: T, message_resource: str, *message_params):
        """
        Checks if the value is greater than or equal to the specified start value and adds an error message if it is not.
        
        Args:
            validation_set: The ValidationSet instance to add the validation to.
            value: The value to validate.
            start: The start value to compare against.
            message_resource: The resource string for the error message.
            message_params: The parameters to format the message.
        
        Returns:
            The updated ValidationSet instance.
        """
        return self.add_validation(self, is_greater_than_or_equal_to(value, min), message_resource, *message_params)

    def add_less_than_validation(self, value: T, end: T, message_resource: str, *message_params):
        """
        Checks if the value is less than the specified end value and adds an error message if it is not.
        
        Args:
            validation_set: The ValidationSet instance to add the validation to.
            value: The value to validate.
            end: The end value to compare against.
            message_resource: The resource string for the error message.
            message_params: The parameters to format the message.
        
        Returns:
            The updated ValidationSet instance.
        """
        return self.add_validation(self, is_less_than(value, end), message_resource, *message_params)

    def add_less_or_equal_to_validation(self, value: T, end: T, message_resource: str, *message_params):
        """
        Checks if the value is less than or equal to the specified end value and adds an error message if it is not.
        
        Args:
            validation_set: The ValidationSet instance to add the validation to.
            value: The value to validate.
            end: The end value to compare against.
            message_resource: The resource string for the error message.
            message_params: The parameters to format the message.
        
        Returns:
            The updated ValidationSet instance.
        """
        return self.add_validation(self, is_less_or_equal_to(value, end), message_resource, *message_params)

    def add_between_validation(self, value: T, start: T, end: T, message_resource: str, *message_params):
        """
        Checks if the value is between the specified limits (inclusive) and adds an error message if it is not.
        
        Args:
            validation_set: The ValidationSet instance to add the validation to.
            value: The value to validate.
            start: The start value of the range.
            end: The end value of the range.
            message_resource: The resource string for the error message.
            message_params: The parameters to format the message.
        
        Returns:
            The updated ValidationSet instance.
        """
        return self.add_validation(self, between(value, start, end), message_resource, *message_params)

    def add_length_between_validation(self, value: str, start: int, end: int, message_resource: str, *message_params):
        """
        Checks if the length of the string is between the specified limits (inclusive) and adds an error message if it is not.
        
        Args:
            validation_set: The ValidationSet instance to add the validation to.
            value: The string value to validate.
            start: The minimum length of the string.
            end: The maximum length of the string.
            message_resource: The resource string for the error message.
            message_params: The parameters to format the message.
        
        Returns:
            The updated ValidationSet instance.
        """
        return self.add_validation(self, length_between(value, start, end), message_resource, *message_params)

    def add_is_not_none_validation(self, obj: Optional[T], message_resource: str, *message_params):
        """
        Checks if the object is not None and adds an error message if it is.
        
        Args:
            validation_set: The ValidationSet instance to add the validation to.
            obj: The object to validate.
            message_resource: The resource string for the error message.
            message_params: The parameters to format the message.
        
        Returns:
            The updated ValidationSet instance.
        """
        return self.add_validation(self, is_not_none(obj), message_resource, *message_params)

    def add_is_not_empty_validation(self, value: str, message_resource: str, *message_params):
        """
        Checks if the string is not empty and adds an error message if it is.
        
        Args:
            validation_set: The ValidationSet instance to add the validation to.
            value: The string value to validate.
            message_resource: The resource string for the error message.
            message_params: The parameters to format the message.
        
        Returns:
            The updated ValidationSet instance.
        """
        return self.add_validation(self, is_not_empty(value), message_resource, *message_params)

    def add_is_not_empty_or_whitespace_validation(self, value: str, message_resource: str, *message_params):
        """
        Checks if the string is not empty or composed only of white spaces and adds an error message if it is.
        
        Args:
            validation_set: The ValidationSet instance to add the validation to.
            value: The string value to validate.
            message_resource: The resource string for the error message.
            message_params: The parameters to format the message.
        
        Returns:
            The updated ValidationSet instance.
        """
        return self.add_validation(self, is_not_empty_or_white_space(value), message_resource, *message_params)

    def add_is_defined_validation(self, value: TEnum, message_resource: str, *message_params):
        """
        Checks if the enum value is defined in the enum type and adds an error message if it is not.
        
        Args:
            validation_set: The ValidationSet instance to add the validation to.
            value: The enum value to validate.
            message_resource: The resource string for the error message.
            message_params: The parameters to format the message.
        
        Returns:
            The updated ValidationSet instance.
        """
        return self.add_validation(self, isinstance(value, TEnum), message_resource, *message_params)

    def add_is_parsed_validation(self, string_value: str, enum_class: type, message_resource: str, *message_params):
        """
        Checks if the string can be parsed into the specified enum type and adds an error message if it cannot.
        
        Args:
            validation_set: The ValidationSet instance to add the validation to.
            string_value: The string value to validate.
            enum_class: The enum class to parse the string into.
            message_resource: The resource string for the error message.
            message_params: The parameters to format the message.
        
        Returns:
            The updated ValidationSet instance.
        """
        try:
            enum_class[string_value]
            return self
        except KeyError:
            message = message_resource.format(*message_params)
            self.add_error(message)
            return self

    def add_validation(self, condition: bool, message_resource: str, *message_params):
        """
        Checks if a condition is met and adds an error message if it is not.
        
        Args:
            validation_set: The ValidationSet instance to add the validation to.
            condition: The condition to check.
            message_resource: The resource string for the error message.
            message_params: The parameters to format the message.
        
        Returns:
            The updated ValidationSet instance.
        """
        if not condition:
            message = message_resource.format(*message_params)
            self.add_error(message)
        return self

    def add_validation_with_condition(self, obj: T, condition: Callable[[T], bool], message_resource: str, *message_params):
        """
        Checks if a condition is met and adds an error message if it is not.
        
        Args:
            validation_set: The ValidationSet instance to add the validation to.
            obj: The object to validate.
            condition: The condition to check.
            message_resource: The resource string for the error message.
            message_params: The parameters to format the message.
        
        Returns:
            The updated ValidationSet instance.
        """
        return self.add_validation(self, condition(obj), message_resource, *message_params)
