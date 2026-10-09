import random

MIN_NUMBER = 1
MAX_NUMBER = 100


def get_random_number(start=MIN_NUMBER, end=MAX_NUMBER):
    return random.randint(start, end)


def to_yes_no(flag):
    return 'yes' if flag else 'no'
