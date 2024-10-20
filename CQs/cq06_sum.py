"""Summing the elements of a list using different loops"""

__author__ = "730752527"


def w_sum(vals: list[float]) -> float:
    """
    Returns the sum of all floats in a list
    """
    i: int = 0
    sum: float = 0.0
    while i < len(vals):
        sum += vals[i]
        i += 1

    return sum


def f_sum(vals: list[float]) -> float:
    """
    Returns the sum of all floats in a list
    """
    sum: int = 0
    for i in vals:
        sum += i  # type: ignore

    return sum


def f_range_sum(vals: list[float]) -> float:
    """
    Returns the sum of all floats in a list
    """
    sum: int = 0
    for i in range(len(vals)):
        sum += vals[i]  # type: ignore

    return sum
