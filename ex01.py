from datetime import datetime


def get_days_from_today(date: str) -> int:
    """
    @brief Calculates the number of days between today and a given date.

    @param date Input date string in "%Y-%m-%d" format.

    @return int Number of days between today and the input date. Positive if the date is in the past, negative if in the future.

    @throws ValueError If the input date string does not match the required format.
    """

    input_date: datetime = datetime.strptime(date, "%Y-%m-%d")

    return (datetime.today().date() - input_date.date()).days
