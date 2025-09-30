import re


def normalize_phone(phone_number: str) -> str:
    """
    @brief Normalizes a phone number to international format.

    @param phone_number Input phone number as a string. Can contain any characters.

    @return str Normalized phone number in the format '+38XXXXXXXXXX'.

    @throws ValueError If the phone number cannot be normalized (not 10 or 12 digits after cleaning).
    """

    # Getting rid of all characters except numbers
    ret = re.sub("[^0-9]", "", phone_number)

    if len(ret) != 10 and len(ret) != 12:
        raise ValueError("Provided number cannot be normalized")

    if re.search("38", ret):
        return "+" + ret
    return "+38" + ret
