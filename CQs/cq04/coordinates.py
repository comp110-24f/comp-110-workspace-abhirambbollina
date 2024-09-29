"""CQ04 - turns two strings into printed coordinates"""

__author__ = "730752527"


def get_coords(xs: str, ys: str) -> None:
    """
    turns two strings into printed coordinates
    """

    i: int = 0
    j: int = 0
    # Uses Nested while loops
    while i < len(xs):
        x = xs[i]
        i += 1
        while j < len(ys):
            y = ys[j]
            print("(" + x + "," + y + ")")
            j += 1
        j = 0
    i = 0
