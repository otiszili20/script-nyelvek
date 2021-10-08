import string
import random


def get_random_pwd(length, use_digit, use_punctuation):

    available_characters = string.ascii_letters
    if use_digit:
        available_characters = available_characters + string.digits
    if use_punctuation:
        available_characters = available_characters + string.punctuation

    password = "".join(random.choice(available_characters) for _ in range(1, length))
    return password


if __name__ == '__main__':
    print(f"generated password: {get_random_pwd(length=9, use_digit=True, use_punctuation=False)}")
