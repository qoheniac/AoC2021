# read all connections into a dictionary
system = dict()
with open("input") as f:
    for line in f:
        path = line.rstrip().split("-")
        for i in range(2):
            if path[i] in system:
                system[path[i]].append(path[i - 1])
            else:
                system[path[i]] = [path[i - 1]]


# function counting all paths from cave to "end" avoiding caves in visited
# if one of them has already been visited twice
def search(cave, visited=[], visited_twice=False):
    if cave == "end":
        return 1
    n = 0
    for neighbor in system[cave]:
        if neighbor not in visited:
            # remember current cave only if not big
            if cave.isupper():
                n += search(neighbor, visited.copy(), visited_twice)
            else:
                n += search(neighbor, visited + [cave], visited_twice)
        elif not visited_twice and neighbor != "start":
            # remember current cave only if not big
            if cave.isupper():
                n += search(neighbor, visited.copy(), True)
            else:
                n += search(neighbor, visited + [cave], True)
    return n


# count all paths from "start" to "end" visiting small caves only once
# or one of them twice but the rest once
print(search("start"))
