from datetime import datetime
from datetime import timedelta


def get_upcoming_birthdays(users: list[dict[str:str]]):
    """
    Returns users whose birthdays are within the next 7 days.

    :param users: List of user dictionaries with "name" and "birthday" keys.
                  The birthday must be in the "YYYY.MM.DD" format.
    :type users: list[dict[str, str]]

    :return: List of dictionaries containing each user's name and the date
             when they should be congratulated (in "YYYY.MM.DD" format).
    :rtype: list[dict[str, str]]

    :raises TypeError: If the input is not of list type.
    :raises ValueError: If data types are invalid, required keys are missing,
                        or birthday format is incorrect.

    :note: Birthdays falling on weekends are moved to the following Monday.
    """

    if not isinstance(users, list):
        raise TypeError("Argument must be a list")

    if not len(users):
        return []

    try:
        if any(
            [
                (type(user["name"]) != str or type(user["birthday"]) != str)
                for user in users
            ]
        ):
            raise ValueError("Incorrect type of data")
    except KeyError:
        raise ValueError("Name or birthday not found in one of users")

    today = datetime.today().date()

    try:
        bdays = [
            datetime.strptime(user["birthday"], "%Y.%m.%d")
            .date()
            .replace(year=today.year)
            for user in users
        ]
    except ValueError as e:
        raise e

    congrat_dates = [
        (
            bday
            if (bday - today) >= timedelta(days=0)
            and (bday - today) <= timedelta(days=7)
            else None
        )
        for bday in bdays
    ]

    SATURDAY = 5
    congrat_dates = [
        (
            date + timedelta(days=7 - date.weekday())
            if date and date.weekday() >= SATURDAY
            else date
        )
        for date in congrat_dates
    ]

    ret = []
    for user, date in zip(users, congrat_dates):
        if date:
            ret.append(
                {
                    "name": user["name"],
                    "congratulation_date": date.strftime("%Y.%m.%d"),
                }
            )

    return ret


# Tests:

if __name__ == "__main__":

    def create_user(name: str, birthday: str) -> dict:
        return {"name": name, "birthday": birthday}

    tests = [
        None,
        123,
        [{"123": 123}],
        [{"123": "123"}],
        [{"name": 123, "birthday": 123}],
        [create_user("Paul", "1990.01.10"), create_user("John", "1990.01.10")],
        [create_user("Paul", "1990.10.5")],
        [create_user("Paul", "1990.10.10"), create_user("Paul", "1990.10.11")],
        [create_user("Paul", "1990.10.12")],
    ]

    for test in tests:
        print(f"In:  {str(test)}", end="\t\t\n")
        print("Out: ", end="")
        try:
            print(get_upcoming_birthdays(test))
        except Exception as e:
            print(e)
        print()
