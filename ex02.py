from random import shuffle


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """
    Generates a sorted list of unique random numbers within a specified range.

    :param min: Minimal value of the range (inclusive). Must be >= 1.
    :type min: int
    :param max: Maximal value of the range (inclusive). Must be <= 1000.
    :type max: int
    :param quantity: Number of random numbers to generate. Must be between min and max (inclusive).
    :type quantity: int

    :return: Sorted list of unique random numbers.
             Returns an empty list if input parameters are out of allowed bounds.
    :rtype: list[int]

    :raises TypeError: If any of the input is not of int type.
    """

    if not all((isinstance(min, int), isinstance(max, int), isinstance(quantity, int))):
        raise TypeError("All arguments must be type of int")

    if min < 1 or max > 1000 or (quantity < min or quantity > max):
        return list()

    ret = list(range(min, max + 1))

    shuffle(ret)

    return sorted(ret[:quantity])


# Tests:

if __name__ == "__main__":

    tests = [
        [None, None, None],
        ["1", "2", "3"],
        [1, 2, 3],
        [0, 1000, 50],
        [1, 1001, 50],
        [1, 20, 50],
        [20, 100, 10],
        [5, 1000, 90],
        [1, 200, 50],
        [80, 1000, 90],
    ]

    for test in tests:
        print(f"{str(test):25}", end="")
        try:
            print(get_numbers_ticket(test[0], test[1], test[2]))
        except Exception as e:
            print(e)
