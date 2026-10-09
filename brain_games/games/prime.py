from brain_games.utils import get_random_number, to_yes_no

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

SMALLEST_PRIME = 2


def is_prime(number):
    if number < SMALLEST_PRIME:
        return False
    divisor = SMALLEST_PRIME
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def generate_round():
    number = get_random_number()
    return str(number), to_yes_no(is_prime(number))
