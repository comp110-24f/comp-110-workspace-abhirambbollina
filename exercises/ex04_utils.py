"""EX04 - List Utility Functions"""

__author__ = "730752527"


def all(checked_list: list[int], check_int: int) -> bool:
    """
    Checks if all of the integers in a
    list are the same as a given integer
    Parameters: checked_list, check_int
    Variables: checked_list, check_int, i
    Return Type: bool
    """

    # Returns false immediatly if any values don't match
    # Returns true if while loop completes
    # becasue this meams that all values are equal
    i: int = 0
    while i < len(checked_list):
        if checked_list[i] != check_int:
            return False
        i += 1

    return True


def max(input: list[int]) -> int:
    """
    Finds the max value in a list of ints
    Parameters: input
    Variables: input, i, max
    Return Type: int
    """
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    # Sets first value of list to max
    # Loops through list and changes max if current value
    # is greater than max
    i: int = 0
    max: int = input[0]
    while i < len(input):
        if input[i] > max:
            max = input[i]
        i += 1

    return max


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """
    Checks if two lists are deeply equal to eachother
    Parameters: list_1, list_2
    Variables: list_1, list_2, i
    Return Type: bool
    """
    # Immediatly returns False if list lengths are not equal
    if len(list_1) != len(list_2):
        return False

    i: int = 0

    # Returns false as soon as any values don't match
    # Returns true if while loop goes through without breaking
    while i < len(list_1):
        if list_1[i] != list_2[i]:
            return False
        i += 1
    return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    """
    Mutates a list by adding all of the values
    of a second list to the end of it
    Parameters: list_1, list_2
    Variables: list_1, list_2, i
    Return Type: None
    """
    i: int = 0

    # Uses a while loop to individually append each
    # value in list_2 to list_1
    while i < len(list_2):
        list_1.append(list_2[i])
        i += 1
