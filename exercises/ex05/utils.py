"""List Utility Functions"""

__author__ = "730752527"


def only_evens(input: list[int]) -> list[int]:
    """
    Name: only_evens
    Arguments: A list of integers.
    Returns: A list of integers, containing
    only the even elements of the input parameter.
    """
    output: list[int] = []

    for num in input:
        if num % 2 == 0:
            output.append(num)
    return output


def sub(input: list[int], start: int, end: int) -> list[int]:
    """
    Name: sub
    Parameters: A list and two ints,
    where the first int serves as a start index
    and the second int serves as an end index
    (not inclusive).
    Returns: A list which is a subset of
    the given list, between the specified start
    index and the end index - 1
    """
    # Edge Cases
    if start >= len(input) or len(input) == 0 or end < 0:
        return []
    if start < 0:
        start = 0
    if end >= len(input):
        end = len(input)

    output: list[int] = []
    i: int = start
    while i < end:
        output.append(input[i])
        i += 1
    return output


def add_at_index(input: list[int], added_int: int, index: int) -> None:
    """
    Name: add_at_index
    Parameters: A list and two ints, where the first
    int is the element to be added and the second int
    is the index at which it should be added.
    Returns: None
    """
    if index < 0 or index >= len(input):
        raise IndexError("Index is out of bounds for the input list")
    input.append(0)
    i: int = len(input) - 2
    while i > index - 1:
        input[i + 1] = input[i]
        i -= 1
    input[index] = added_int
