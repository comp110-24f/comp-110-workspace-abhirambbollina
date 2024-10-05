"""While loop Challenge Question"""

__author__ = "730752527"


def num_instances(phrase: str, search_char: str) -> int:
    """
    Iterates through phrase looking for
    instances of search_char
    """
    word_length = len(phrase)
    # Iteration variable
    i = 0
    count = 0

    # i goes up by one each loop until i exceeds word_length
    while i < word_length:
        # Conditional to check if the character at
        # index i matches the search_character
        if phrase[i] == search_char:
            count += 1
        i += 1
    return count
