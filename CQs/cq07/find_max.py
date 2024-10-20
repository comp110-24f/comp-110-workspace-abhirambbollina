__author__ = "730752527"


def find_and_remove_max(input: list[int]) -> int:
    """
    will take a list[int] as input and return an int
    will find and return the largest number in the input list
    will also remove all instances of the largest number from the input list
    If the input list is empty, return -1 and doesn't modify the input list
    """
    if len(input) == 0:
        return -1
    max: int = input[0]

    for num in input:
        if num > max:
            max = num
    i: int = 0

    while i < len(input):
        if input[i] == max:
            input.pop(i)
            i -= 1
        i += 1

    return max
