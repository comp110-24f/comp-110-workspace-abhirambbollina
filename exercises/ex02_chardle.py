"""EX02 - Chardle Exercise"""

__author__ = "730752527"


def input_word() -> str:
    """
    Prompts user for a 5 character word
    and checks for a valid input
    """
    user_word = input("Enter a 5-character word: ")
    # exits if user gives invalid input
    if len(user_word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return user_word


def input_letter() -> str:
    """
    Prompts user for a single character
    and checks for a valid input
    """
    user_letter = input("Enter a single character: ")
    # exits if user gives invalid input
    if len(user_letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return user_letter


def contains_char(word: str, letter: str) -> None:
    """
    Checks if as well as how many times letter is in word,
    printing different statemts for each case
    """
    print("Searching for " + letter + " in " + word)
    instances = 0

    # 5 if statements to check each character of word to see if matches letter
    if word[0] == letter:
        print(letter + " found at index 0")
        instances += 1
    if word[1] == letter:
        print(letter + " found at index 1")
        instances += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        instances += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        instances += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        instances += 1

    # 3 cases; 1 vs >1 vs 0
    if instances == 1:
        print("1 instance of " + letter + " found in " + word)
    elif instances != 0:
        print(str(instances) + " instances of " + letter + " found in " + word)
    else:
        print("No instances of " + letter + " found in " + word)


def main() -> None:
    """
    Entrypoint of Program
    """
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
