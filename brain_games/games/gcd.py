from brain_games.utils import get_random_number

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def find_gcd(first, second):
    while second:
        first, second = second, first % second
    return first


def generate_round():
    first = get_random_number()
    second = get_random_number()
    return f'{first} {second}', str(find_gcd(first, second))
