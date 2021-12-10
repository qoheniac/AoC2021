from numpy import array, full

# read input
with open("input", "r") as f:
    numbers = f.read().splitlines()
numbers = array([[int(c) for c in line] for line in numbers])

# find answer
answ = 1
for compare in [lambda a, b: a == b, lambda a, b: a != b]:
    mask = full(numbers.shape[0], True)
    for i in range(numbers.shape[1]):
        ones = sum(numbers[mask, i])
        common = 1 if ones >= numbers[mask].shape[0] / 2 else 0
        mask[mask] = [compare(num, common) for num in numbers[mask, i]]
        if sum(mask) == 1:
            break
    answ *= sum([n * 2 ** i for i, n in enumerate(numbers[mask][0][::-1])])
print(answ)
