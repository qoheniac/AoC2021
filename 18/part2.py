from tqdm import trange
from copy import deepcopy


# states: 0 not exploded | 1 exploded | 2 done
def explode(number, depth=0, state=0, mem=None):
    for i, number_i in enumerate(number):

        # regular number
        if not isinstance(number_i, list):
            match state:
                case 0:
                    mem = [number, i]
                case 1:
                    number[i] += mem
                    return 2, None

        # snailfish number
        else:
            if depth == 3:
                match state:
                    case 0:
                        if mem is not None:
                            mem[0][mem[1]] += number_i[0]
                        mem = number_i[1]
                        number[i] = 0
                        state = 1
                    case 1:
                        number_i[0] += mem
                        return 2, None
            else:
                state, mem = explode(number_i, depth + 1, state, mem)
                if state == 2:
                    return 2, None

    return state, mem


def split(number):
    for i, number_i in enumerate(number):

        # regular number
        if not isinstance(number_i, list):
            if number_i >= 10:
                number[i] = [number_i // 2, int(number_i / 2 + 0.5)]
                return 1

        # snailfish number
        else:
            if split(number_i) == 1:
                return 1

    return 0


def reduce(number):
    while True:
        if explode(number)[0] == 0:  # not exploded
            if split(number) == 0:  # not split
                break


def magnitude(number):
    if isinstance(number, list):
        return 3 * magnitude(number[0]) + 2 * magnitude(number[-1])
    else:
        return number


# read homework
with open("input") as f:
    homework = [eval(line.rstrip()) for line in f]
N = len(homework)

# calculate sums and print maximum magnitude
maxmag = 0
for i in trange(N):
    for j in range(N):
        if i == j:
            continue
        result = [deepcopy(homework[i]), deepcopy(homework[j])]
        reduce(result)
        maxmag = max(maxmag, magnitude(result))
print(maxmag)
