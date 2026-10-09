from brain_games.utils import get_random_number

DESCRIPTION = 'What number is missing in the progression?'

PROGRESSION_LENGTH = 10
MIN_STEP = 1
MAX_STEP = 10
HIDDEN_MARK = '..'


def make_progression(start, step, length):
    return [start + index * step for index in range(length)]


def generate_round():
    start = get_random_number()
    step = get_random_number(MIN_STEP, MAX_STEP)
    progression = make_progression(start, step, PROGRESSION_LENGTH)
    hidden_index = get_random_number(0, PROGRESSION_LENGTH - 1)
    answer = progression[hidden_index]
    items = [str(item) for item in progression]
    items[hidden_index] = HIDDEN_MARK
    return ' '.join(items), str(answer)
