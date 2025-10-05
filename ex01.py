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
