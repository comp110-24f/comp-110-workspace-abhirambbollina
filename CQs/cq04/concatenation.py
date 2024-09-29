"""CQ04 - concatonates two strings"""

__author__ = "730752527"


def concat(str1: str, str2: str) -> str:
    """
    Returns the concatonation of 2 strings
    """
    return str1 + str2


if __name__ == "__main__":
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(str1=word1, str2=word2))
