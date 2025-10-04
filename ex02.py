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
    """

    if min < 1 or max > 1000 or (quantity < min or quantity > max):
        return list()

    ret = list(range(min, max + 1))

    shuffle(ret)

    return sorted(ret[:quantity])
