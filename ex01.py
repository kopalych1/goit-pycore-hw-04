from datetime import datetime


def get_days_from_today(date: str) -> int:
    """
    Calculates the number of days between today and a given date.

    :param date: Input date string in the "%Y-%m-%d" format.
    :type date: str

    :return: Number of days between today and the input date.
             Positive if the date is in the past, negative if in the future.
    :rtype: int

    :raises TypeError: If the input is not of string type.
    :raises ValueError: If the input date string does not match the required format.
    """

    if not isinstance(date, str):
        raise TypeError("Argument must be a string in '%Y-%m-%d' format")

    try:
        input_date: datetime = datetime.strptime(date, "%Y-%m-%d")
    except ValueError as e:
        raise ValueError(f"String '{date}' does not match format '%Y-%m-%d'") from e

    return (datetime.today().date() - input_date.date()).days


# Tests:

if __name__ == "__main__":
    tests = [
        None,
        123,
        "",
        " ",
        "---",
        "123",
        "05.10.2025",
        "05/10/2025",
        "055446552025",
        "0554406-552025",
        "0554-06552025",
        "0554-06-552025",
        "0554-06-abc",
        "2025-10-1",
        "2025-1-20",
        "102-1-20",
        "0102-1-20",
        "2025-10-01",
        "2025-10-10",
    ]

    for test in tests:
        print(f"{str(test):20}", end="")
        try:
            print(get_days_from_today(test))
        except Exception as e:
            print(e)
