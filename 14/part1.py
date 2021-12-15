# read template, rules and elements
with open("input") as f:
    polymer = f.readline().rstrip()
    f.readline()
    rules = dict()
    for line in f:
        pair, element = line.rstrip().split(" -> ")
        rules[pair] = element
elements = set(list(polymer) + list(rules.values()))

# polymerize
for _ in range(10):
    old_polymer, polymer = polymer, polymer[0]
    for i in range(len(old_polymer) - 1):
        if (pair := old_polymer[i : i + 2]) in rules:
            polymer += rules[pair]
        polymer += old_polymer[i + 1]

# count quantity of different elements in polymer
counts = dict()
for element in elements:
    counts[element] = 0
for element in polymer:
    counts[element] += 1

# output difference between largest and smallest quantities
values = sorted(counts.values())
print(values[-1] - values[0])
