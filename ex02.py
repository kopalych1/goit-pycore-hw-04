from random import shuffle


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """
    @brief Generates a sorted list of unique random numbers within a specified range.

    @param min Minimal value of the range (inclusive). Must be >= 1.
    @param max Maximal value of the range (inclusive). Must be <= 1000.
    @param quantity Number of random numbers to generate. Must be between min and max (inclusive)

    @return list[int] Sorted list of unique random numbers.
            Returns an empty list if input parameters are out of allowed bounds.

    """

    if min < 1 or max > 1000 or (quantity < min or quantity > max):
        return list()

    ret = list(range(min, max + 1))

    shuffle(ret)

    return sorted(ret[:quantity])
