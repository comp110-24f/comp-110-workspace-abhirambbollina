"""Lists Challenge Question"""

__author__ = "730752527"


def manual_append(int_list: list[int], append_int: int) -> None:
    """
    Manually appends the int to the list by
    using the append function

    Variables: int_list, append_int
    Parameters: : int_list, append_int
    Return Type: None
    """
    int_list.append(append_int)


def double(doubled_list: list[int]) -> None:
    """
    Uses a while loop to double each
    integer in the list using index i

    Variables: doubled_list, i
    Parameters: : doubled_list
    Return Type: None
    """
    i: int = 0
    while i < len(doubled_list):
        doubled_list[i] = 2 * doubled_list[i]
        i += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
