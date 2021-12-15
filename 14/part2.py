# read template, rules and elements
with open("input") as f:
    template = f.readline().rstrip()
    f.readline()
    rules = dict()
    for line in f:
        pair, element = line.rstrip().split(" -> ")
        rules[pair] = element
elements = set(list(template) + list(rules.values()))

# initialize counters for all possible pairs
pairs_count = dict()
for first in elements:
    for second in elements:
        pairs_count[first + second] = 0

# add pairs in template to corresponding counters
for i in range(len(template) - 1):
    pairs_count[template[i] + template[i + 1]] += 1

# polymerize
for _ in range(40):
    old_pairs_count = pairs_count.copy()
    for pair, element in rules.items():
        if (c := old_pairs_count[pair]) != 0:
            pairs_count[pair] -= c
            pairs_count[pair[0] + element] += c
            pairs_count[element + pair[1]] += c

# initialize dict for doubled element quantities with zeros
# (doubled because each atom belongs to two neighboring pairs)
double_counts = dict()
for element in elements:
    double_counts[element] = 0

# add one for atoms at ends because they only belong to one pair each
double_counts[template[0]] = 1
double_counts[template[-1]] = 1

# add pair counts to both corresponding elements
for (first, second), count in pairs_count.items():
    double_counts[first] += count
    double_counts[second] += count

# output difference between largest and smallest quantities
values = sorted(double_counts.values())
print((values[-1] - values[0]) // 2)
