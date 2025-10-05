import re


def normalize_phone(phone_number: str) -> str:
    """
    Normalizes a phone number to international format.

    :param phone_number: Input phone number as a string. Can contain any characters.
    :type phone_number: str

    :return: Normalized phone number in the format "+38XXXXXXXXXX".
    :rtype: str

    :raises TypeError: If the input is not of string type.
    :raises ValueError: If the phone number cannot be normalized
                        (not 10 or 12 digits after cleaning).
    """

    if not isinstance(phone_number, str):
        raise TypeError("Argument must be a string")

    # Getting rid of all characters except numbers
    ret = re.sub("[^0-9]", "", phone_number)

    if not (len(ret) == 10 or (len(ret) == 12 and ret[0:2] == "38")):
        raise ValueError("Provided number cannot be normalized")

    if re.search("38", ret):
        return "+" + ret
    return "+38" + ret


# Tests:

if __name__ == "__main__":
    tests = [
        None,
        123,
        "",
        " ",
        "38489484512984",
        "38489484512",
        "3848948451211",
        "384894845122",
        "34894845122",
        "4894845122",
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    for test in tests:
        print(f"{str(test):25}", end="")
        try:
            print(normalize_phone(test))
        except Exception as e:
            print(e)
