from typing import TypeVar
T = TypeVar('T')

def is_greater_than(value: T, min: T) -> bool:
    """
    Checks if the value is greater than the specified start (exclusive).
    
    Args:
        value (T): The value to compare.
        start (T): The start value to compare with.
    
    Returns:
        bool: True if value is greater than start, otherwise False.
    """
    return value > min


def is_greater_than_or_equal_to(value: T, start: T) -> bool:
    """
    Checks if the value is greater than or equal to the specified start (inclusive).
    
    Args:
        value (T): The value to compare.
        start (T): The start value to compare with.
    
    Returns:
        bool: True if value is greater than or equal to start, otherwise False.
    """
    return value >= start


def is_less_than(value: T, end: T) -> bool:
    """
    Checks if the value is less than the specified end (exclusive).
    
    Args:
        value (T): The value to compare.
        end (T): The end value to compare with.
    
    Returns:
        bool: True if value is less than end, otherwise False.
    """
    return value < end


def is_less_or_equal_to(value: T, end: T) -> bool:
    """
    Checks if the value is less than or equal to the specified end (inclusive).
    
    Args:
        value (T): The value to compare.
        end (T): The end value to compare with.
    
    Returns:
        bool: True if value is less than or equal to end, otherwise False.
    """
    return value <= end


def between(value: T, start: T, end: T) -> bool:
    """
    Checks if the value is between the specified limits (inclusive).
    
    Args:
        value (T): The value to check.
        start (T): The start value to compare with.
        end (T): The end value to compare with.
    
    Returns:
        bool: True if value is between start and end (inclusive), otherwise False.
    """
    return start <= value <= end


def length_between(value: str, start: int, end: int) -> bool:
    """
    Checks if the length of the string is between the specified limits (inclusive).
    
    Args:
        value (str): The string whose length is being checked.
        start (int): The minimum length.
        end (int): The maximum length.
    
    Returns:
        bool: True if the length of the string is between start and end (inclusive), otherwise False.
    """
    return start <= len(value) <= end


def is_not_none(obj: T) -> bool:
    """
    Checks if the object is not null.
    
    Args:
        obj (T): The object to check.
    
    Returns:
        bool: True if the object is not null, otherwise False.
    """
    return obj is not None


def is_not_empty(value: str) -> bool:
    """
    Checks if the string is not empty.
    
    Args:
        value (str): The string to check.
    
    Returns:
        bool: True if the string is not empty, otherwise False.
    """
    return bool(value)


def is_not_empty_or_white_space(value: str) -> bool:
    """
    Checks if the string is not empty or composed only of white spaces.
    
    Args:
        value (str): The string to check.
    
    Returns:
        bool: True if the string is neither null, empty, nor whitespace, otherwise False.
    """
    return bool(value and not value.isspace())
