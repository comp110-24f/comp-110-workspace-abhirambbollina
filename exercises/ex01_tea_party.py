"""Program to facilitate a tea party"""

__author__ = "730752527"


def main_planner(guests: int) -> None:
    """Entrypoint of the program"""

    # converts all function outputs and ints to strings to concatanate with the other strings
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    # Uses tea_bags function and treats function to calcualate cost
    print("Cost: " + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """calcualtes the number of teabags needed for the party"""
    return people * 2


def treats(people: int) -> int:
    """calcualtes the number of treats needed for the party"""
    return int(tea_bags(people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """colculates total cost of the party given numbver of tea bags and treats"""
    return (tea_count * 0.50) * (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
