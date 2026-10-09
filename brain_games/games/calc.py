import operator
import random

from brain_games.utils import get_random_number

DESCRIPTION = 'What is the result of the expression?'

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def generate_round():
    first = get_random_number()
    second = get_random_number()
    sign = random.choice(list(OPERATIONS))
    result = OPERATIONS[sign](first, second)
    return f'{first} {sign} {second}', str(result)
