from brain_games.utils import get_random_number, to_yes_no

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_round():
    number = get_random_number()
    return str(number), to_yes_no(is_even(number))
