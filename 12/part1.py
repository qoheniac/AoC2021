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
def search(cave, visited=[]):
    if cave == "end":
        return 1
    n = 0
    for neighbor in system[cave]:
        if neighbor not in visited:
            # remember current cave only if not big
            if cave.isupper():
                n += search(neighbor, visited.copy())
            else:
                n += search(neighbor, visited + [cave])
    return n


# count all paths from "start" to "end" visiting small caves only once
print(search("start"))
